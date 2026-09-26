"""Trace shape and metrics for one agent run (fake Messages API, no network)."""
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.sdk.trace.export.in_memory_span_exporter import InMemorySpanExporter
from prometheus_client import REGISTRY

from rag.observability import record_run
from tests.test_agent import FakeClient, answer_call, msg, run, text, tool, verdict

EXPORTER = InMemorySpanExporter()
provider = trace.get_tracer_provider()
if not isinstance(provider, TracerProvider):  # nothing installed yet in this process
    provider = TracerProvider()
    trace.set_tracer_provider(provider)
provider.add_span_processor(SimpleSpanProcessor(EXPORTER))


def metric(name, **labels):
    return REGISTRY.get_sample_value(name, labels) or 0.0


def test_spans_nest_under_one_trace(make_agent):
    EXPORTER.clear()
    client = FakeClient(
        [msg(text("Searching."), tool("search_conversations", {"query": "locked", "company": "Delta"}, "t1")),
         msg(answer_call("t2"))],
        [verdict(True)])
    run(make_agent(client))
    spans = {s.name: s for s in EXPORTER.get_finished_spans()}
    root = spans["agent.run"]
    assert root.parent is None or root.parent.span_id != root.context.span_id
    trace_ids = {s.context.trace_id for s in spans.values()}
    assert trace_ids == {root.context.trace_id}
    by_id = {s.context.span_id: s for s in EXPORTER.get_finished_spans()}
    parent = lambda s: by_id[s.parent.span_id].name  # noqa: E731
    agent_calls = [s for s in EXPORTER.get_finished_spans() if s.name == "llm.agent"]
    assert len(agent_calls) == 2 and all(parent(s) == "agent.run" for s in agent_calls)
    assert parent(spans["tool.search_conversations"]) == "agent.run"
    assert parent(spans["llm.verifier"]) == "tool.submit_answer"
    assert agent_calls[0].attributes["gen_ai.usage.input_tokens"] == 100
    assert root.attributes["rag.verified"] is True


def test_llm_and_tool_metrics(make_agent):
    before_cost = metric("rag_llm_cost_usd_total", model="claude-opus-5", role="verifier")
    before_tools = metric("rag_tool_calls_total", tool="submit_answer", status="ok")
    client = FakeClient([msg(answer_call("t1"))], [verdict(True)])
    events = run(make_agent(client))
    assert metric("rag_llm_cost_usd_total", model="claude-opus-5", role="verifier") > before_cost
    assert metric("rag_tool_calls_total", tool="submit_answer", status="ok") == before_tools + 1

    searches, useful = metric("rag_searches_total"), metric("rag_searches_useful_total")
    events.insert(0, type(events[0])("tool_result", {"name": "search_conversations",
                                                     "hits": [{"conversation_id": 317108}]}))
    events.insert(0, type(events[0])("tool_result", {"name": "search_conversations",
                                                     "hits": [{"conversation_id": 5}]}))
    assert record_run(events, 4.2) == "verified"
    assert metric("rag_searches_total") == searches + 2
    assert metric("rag_searches_useful_total") == useful + 1
