"""Model providers behind one small interface.

The agent, verifier and judge only see:
  conv = llm.start(question)                  # new conversation
  turn = await llm.step(conv, model, effort)  # one model turn -> Turn
  llm.add_tool_results(conv, results)         # [(call_id, content, is_error)]
  llm.add_user_text(conv, text)
  data, turn = await llm.structured(model, effort, system, prompt, schema)

Tools are given once, provider-neutral: {"name", "description", "schema"}.

AnthropicLLM uses the Messages API (strict tools, adaptive thinking, prompt
caching, server-side refusal fallback). ResponsesLLM uses the Responses API
through the OpenAI SDK and chains turns with previous_response_id; XaiLLM points
it at xAI and takes the billed cost from usage.cost_in_usd_ticks, OpenAILLM
points it at OpenAI (cost from the price table).
"""
import json
from dataclasses import dataclass, field

from rag.config import PRICES, settings


@dataclass
class Usage:
    input_tokens: int = 0            # uncached input
    output_tokens: int = 0           # includes reasoning
    cache_read_input_tokens: int = 0
    cache_creation_input_tokens: int = 0


@dataclass
class ToolCall:
    id: str
    name: str
    input: dict | None               # None when the arguments weren't valid JSON
    raw: str = ""


@dataclass
class Turn:
    stop_reason: str                 # tool_use | end_turn | refusal | max_tokens
    model: str
    usage: Usage
    cost_usd: float
    text: list[str] = field(default_factory=list)
    thinking: list[str] = field(default_factory=list)
    tool_calls: list[ToolCall] = field(default_factory=list)


def price_cost(model: str, u: Usage) -> float:
    p_in, p_out, p_read, p_write = PRICES.get(model, (0, 0, 0, 0))
    return (u.input_tokens * p_in + u.output_tokens * p_out + u.cache_read_input_tokens * p_read
            + u.cache_creation_input_tokens * p_write) / 1e6


class AnthropicLLM:
    BETAS = ["server-side-fallback-2026-07-01"]

    def __init__(self, system: str, tools: list[dict], client=None):
        import anthropic

        self.client = client or anthropic.AsyncAnthropic()
        self.system = system
        self.tools = [{"name": t["name"], "description": t["description"], "strict": True,
                       "input_schema": t["schema"]} for t in tools]

    def start(self, question: str):
        return [{"role": "user", "content": question}]

    async def _create(self, model, effort, **kw):
        return await self.client.beta.messages.create(
            model=model, max_tokens=16000, betas=self.BETAS, fallbacks="default",
            output_config={"effort": effort, **kw.pop("output_config", {})}, **kw)

    @staticmethod
    def _turn(resp) -> Turn:
        u = resp.usage
        usage = Usage(u.input_tokens or 0, u.output_tokens or 0, u.cache_read_input_tokens or 0,
                      u.cache_creation_input_tokens or 0)
        turn = Turn(stop_reason=resp.stop_reason, model=resp.model, usage=usage,
                    cost_usd=price_cost(resp.model, usage))
        for b in resp.content:
            if b.type == "text" and b.text.strip():
                turn.text.append(b.text)
            elif b.type == "thinking" and b.thinking:
                turn.thinking.append(b.thinking)
            elif b.type == "tool_use":
                turn.tool_calls.append(ToolCall(b.id, b.name, b.input))
        return turn

    async def step(self, messages, model, effort) -> Turn:
        resp = await self._create(model, effort, system=self.system, tools=self.tools, messages=messages,
                                  thinking={"type": "adaptive", "display": "summarized"},
                                  cache_control={"type": "ephemeral"})
        messages.append({"role": "assistant", "content": resp.content})
        return self._turn(resp)

    def add_tool_results(self, messages, results):
        messages.append({"role": "user", "content": [
            {"type": "tool_result", "tool_use_id": cid, "content": content, **({"is_error": True} if err else {})}
            for cid, content, err in results]})

    def add_user_text(self, messages, text):
        messages.append({"role": "user", "content": text})

    async def structured(self, model, effort, system, prompt, schema):
        resp = await self._create(model, effort, system=system, messages=[{"role": "user", "content": prompt}],
                                  output_config={"format": {"type": "json_schema", "schema": schema}})
        turn = self._turn(resp)
        if resp.stop_reason == "refusal" or not turn.text:
            return None, turn
        return json.loads(turn.text[0]), turn


class ResponsesLLM:
    """Responses API through the OpenAI SDK. xAI serves the same API at its own base URL."""
    BASE_URL = None  # the SDK's default (OpenAI)

    def __init__(self, system: str, tools: list[dict], client=None):
        if client is None:
            import openai

            client = openai.AsyncOpenAI(api_key=self.api_key(), base_url=self.BASE_URL)
        self.client = client
        self.system = system
        # Tool inputs are validated by the caller (xAI doesn't document strict tool schemas).
        self.tools = [{"type": "function", "name": t["name"], "description": t["description"],
                       "parameters": t["schema"]} for t in tools]

    @staticmethod
    def api_key():
        return settings.openai_api_key

    def start(self, question: str):
        # Server-side state: each request sends only new input items plus previous_response_id.
        return {"prev": None, "pending": [{"role": "system", "content": self.system},
                                          {"role": "user", "content": question}]}

    @staticmethod
    def _turn(resp) -> Turn:
        u = resp.usage
        cached = getattr(getattr(u, "input_tokens_details", None), "cached_tokens", 0) or 0
        usage = Usage(input_tokens=(u.input_tokens or 0) - cached, output_tokens=u.output_tokens or 0,
                      cache_read_input_tokens=cached)
        ticks = getattr(u, "cost_in_usd_ticks", None)
        cost = ticks / 1e10 if ticks is not None else price_cost(resp.model, usage)
        turn = Turn(stop_reason="end_turn", model=resp.model, usage=usage, cost_usd=cost)
        for item in resp.output:
            if item.type == "message":
                turn.text += [c.text for c in item.content if getattr(c, "type", "") == "output_text" and c.text.strip()]
            elif item.type == "reasoning":
                turn.thinking += [s.text for s in (getattr(item, "summary", None) or []) if getattr(s, "text", "")]
            elif item.type == "function_call":
                try:
                    args = json.loads(item.arguments)
                except json.JSONDecodeError:
                    args = None
                turn.tool_calls.append(ToolCall(item.call_id, item.name, args, item.arguments))
        if turn.tool_calls:
            turn.stop_reason = "tool_use"
        elif getattr(resp, "status", "completed") == "incomplete":
            turn.stop_reason = "max_tokens"
        return turn

    async def step(self, conv, model, effort) -> Turn:
        resp = await self.client.responses.create(
            model=model, input=conv["pending"], tools=self.tools, previous_response_id=conv["prev"],
            reasoning={"effort": effort}, max_output_tokens=16000, store=True)
        conv["prev"], conv["pending"] = resp.id, []
        return self._turn(resp)

    def add_tool_results(self, conv, results):
        conv["pending"] += [{"type": "function_call_output", "call_id": cid, "output": content}
                            for cid, content, _ in results]

    def add_user_text(self, conv, text):
        conv["pending"].append({"role": "user", "content": text})

    async def structured(self, model, effort, system, prompt, schema):
        resp = await self.client.responses.create(
            model=model, input=[{"role": "system", "content": system}, {"role": "user", "content": prompt}],
            text={"format": {"type": "json_schema", "name": "result", "schema": schema, "strict": True}},
            reasoning={"effort": effort}, max_output_tokens=16000, store=False)
        turn = self._turn(resp)
        if not turn.text:
            return None, turn
        return json.loads(turn.text[0]), turn


class XaiLLM(ResponsesLLM):
    BASE_URL = "https://api.x.ai/v1"

    @staticmethod
    def api_key():
        return settings.xai_api_key


class OpenAILLM(ResponsesLLM):
    pass


def make_llm(system: str, tools: list[dict]):
    if settings.llm_provider == "anthropic":
        return AnthropicLLM(system, tools)
    if settings.llm_provider == "xai":
        return XaiLLM(system, tools)
    if settings.llm_provider == "openai":
        return OpenAILLM(system, tools)
    raise ValueError(f"unknown llm_provider {settings.llm_provider!r}")


def validate(value, schema: dict, path: str = "input") -> list[str]:
    """Checks a tool input against the small JSON Schema subset our tools use
    (object / string / integer / boolean / array, required, enum, additionalProperties)."""
    t = schema.get("type")
    errors = []
    if t == "object":
        if not isinstance(value, dict):
            return [f"{path} must be an object"]
        props = schema.get("properties", {})
        errors += [f"{path}.{k} is required" for k in schema.get("required", []) if k not in value]
        if schema.get("additionalProperties") is False:
            errors += [f"{path}.{k} is not allowed" for k in value if k not in props]
        for k, v in value.items():
            if k in props:
                errors += validate(v, props[k], f"{path}.{k}")
    elif t == "array":
        if not isinstance(value, list):
            return [f"{path} must be an array"]
        for i, v in enumerate(value):
            errors += validate(v, schema.get("items", {}), f"{path}[{i}]")
    elif t == "string" and not isinstance(value, str):
        errors.append(f"{path} must be a string")
    elif t == "integer" and (not isinstance(value, int) or isinstance(value, bool)):
        errors.append(f"{path} must be an integer")
    elif t == "boolean" and not isinstance(value, bool):
        errors.append(f"{path} must be a boolean")
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path} must be one of the allowed values")
    return errors
