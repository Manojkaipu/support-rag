"""Tracing and metrics.

Traces: one trace per question (agent.run), with spans for every model call
(gen_ai.* attributes: model, tokens), tool call, verification and retrieval
stage. Exported over OTLP when OTEL_EXPORTER_OTLP_ENDPOINT is set; otherwise
spans are created but dropped.

Metrics (Prometheus, served at /metrics):
  rag_ask_seconds                     end-to-end latency per question, by outcome
  rag_answers_total                   verified | unverified | unanswerable | failed
  rag_llm_call_seconds                per model call, by role (agent | verifier)
  rag_llm_tokens_total                by model, role, kind (input | output | cache_read | cache_write)
  rag_llm_cost_usd_total              by model, role
  rag_tool_calls_total                by tool and status
  rag_retrieval_seconds               by stage (vector | bm25 | fuse)
  rag_searches_total / rag_searches_useful_total
      a search is useful when one of its conversations is cited by the accepted
      answer; useful / total is the online retrieval hit rate
"""
import os

from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from prometheus_client import Counter, Histogram

tracer = trace.get_tracer("support-rag")

ASK_SECONDS = Histogram("rag_ask_seconds", "End-to-end time to answer a question", ["outcome"],
                        buckets=(2, 5, 10, 20, 30, 45, 60, 90, 120, 180, 300))
ANSWERS = Counter("rag_answers_total", "Answers by outcome", ["outcome"])
LLM_SECONDS = Histogram("rag_llm_call_seconds", "Model call latency", ["role"],
                        buckets=(0.5, 1, 2, 4, 8, 15, 30, 60, 120))
LLM_TOKENS = Counter("rag_llm_tokens_total", "Tokens by model, role and kind", ["model", "role", "kind"])
LLM_COST = Counter("rag_llm_cost_usd_total", "Model spend in USD", ["model", "role"])
TOOL_CALLS = Counter("rag_tool_calls_total", "Agent tool calls", ["tool", "status"])
RETRIEVAL_SECONDS = Histogram("rag_retrieval_seconds", "Retrieval stage latency", ["stage"],
                              buckets=(0.001, 0.0025, 0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1))
SEARCHES = Counter("rag_searches_total", "search_conversations calls in answered runs")
USEFUL_SEARCHES = Counter("rag_searches_useful_total", "Searches that returned a conversation the answer cited")


def setup_tracing(service: str = "support-rag-api"):
    """Installs a tracer provider; exports over OTLP/HTTP when an endpoint is configured."""
    provider = TracerProvider(resource=Resource.create({"service.name": service}))
    if os.environ.get("OTEL_EXPORTER_OTLP_ENDPOINT"):
        from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
        from opentelemetry.sdk.trace.export import BatchSpanProcessor
        provider.add_span_processor(BatchSpanProcessor(OTLPSpanExporter()))
    trace.set_tracer_provider(provider)
    return provider


def record_llm_call(role: str, model: str, usage, cost: float, seconds: float, span=None):
    kinds = {"input": usage.input_tokens, "output": usage.output_tokens,
             "cache_read": usage.cache_read_input_tokens, "cache_write": usage.cache_creation_input_tokens}
    for kind, n in kinds.items():
        if n:
            LLM_TOKENS.labels(model, role, kind).inc(n)
    LLM_COST.labels(model, role).inc(cost)
    LLM_SECONDS.labels(role).observe(seconds)
    if span is not None:
        from rag.config import settings

        span.set_attributes({
            "gen_ai.system": settings.llm_provider, "gen_ai.response.model": model,
            "gen_ai.usage.input_tokens": (usage.input_tokens or 0) + (usage.cache_read_input_tokens or 0),
            "gen_ai.usage.output_tokens": usage.output_tokens or 0,
            "gen_ai.usage.cache_read_input_tokens": usage.cache_read_input_tokens or 0,
            "rag.cost_usd": cost,
        })


def record_run(events, seconds: float):
    """Per-question metrics, computed from the run's event stream."""
    answer = next((e.data for e in events if e.type == "answer"), None)
    if answer is None:
        outcome = "failed"
    elif not answer["answerable"]:
        outcome = "unanswerable"
    else:
        outcome = "verified" if answer["verified"] else "unverified"
    ANSWERS.labels(outcome).inc()
    ASK_SECONDS.labels(outcome).observe(seconds)
    if answer is None:
        return outcome
    cited = set(answer["cited_conversation_ids"])
    for e in events:
        if e.type == "tool_result" and e.data.get("name") == "search_conversations" and "hits" in e.data:
            SEARCHES.inc()
            if cited & {h["conversation_id"] for h in e.data["hits"]}:
                USEFUL_SEARCHES.inc()
    return outcome
