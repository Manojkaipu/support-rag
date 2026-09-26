import type { AgentEvent, Answer, Hit, Usage } from "./api";

export type Step =
  | { kind: "thinking" | "text"; text: string }
  | { kind: "search"; id: string; query: string; company: string; hits?: Hit[]; error?: string }
  | { kind: "open"; id: string; conversationId: number; company?: string; turns?: number; error?: string }
  | { kind: "submit"; id: string }
  | { kind: "verify"; attempt: number; supported: boolean; claims: string[]; feedback: string }
  | { kind: "error"; reason: string };

export type Run = {
  key: string;
  question: string;
  runId?: string;
  steps: Step[];
  hits: Map<number, Hit>; // every conversation retrieved during the run, first sighting wins
  answer?: Answer;
  usage?: Usage;
  status: "running" | "done" | "failed";
};

/** Folds one streamed event into the run (returns a new object for React). */
export function applyEvent(run: Run, ev: AgentEvent): Run {
  const next: Run = { ...run, steps: [...run.steps], hits: run.hits };
  switch (ev.type) {
    case "run":
      next.runId = ev.data.run_id;
      break;
    case "thinking":
    case "text":
      next.steps.push({ kind: ev.type, text: ev.data.text });
      break;
    case "tool_call": {
      const { id, name, input } = ev.data;
      if (name === "search_conversations")
        next.steps.push({ kind: "search", id, query: String(input.query), company: String(input.company) });
      else if (name === "get_conversation")
        next.steps.push({ kind: "open", id, conversationId: Number(input.conversation_id) });
      else if (name === "submit_answer") next.steps.push({ kind: "submit", id });
      break;
    }
    case "tool_result": {
      const i = next.steps.findIndex((s) => "id" in s && s.id === ev.data.id);
      if (i < 0) break;
      const step = next.steps[i];
      if (step.kind === "search") {
        next.steps[i] = { ...step, hits: ev.data.hits, error: ev.data.error };
        if (ev.data.hits) {
          next.hits = new Map(run.hits);
          for (const h of ev.data.hits) if (!next.hits.has(h.conversation_id)) next.hits.set(h.conversation_id, h);
        }
      } else if (step.kind === "open") {
        next.steps[i] = { ...step, company: ev.data.company, turns: ev.data.turns, error: ev.data.error };
      }
      break;
    }
    case "verification":
      next.steps.push({
        kind: "verify",
        attempt: ev.data.attempt,
        supported: ev.data.supported,
        claims: ev.data.unsupported_claims,
        feedback: ev.data.feedback,
      });
      break;
    case "answer":
      next.answer = ev.data;
      break;
    case "usage":
      next.usage = ev.data;
      break;
    case "error":
      next.steps.push({ kind: "error", reason: ev.data.reason });
      break;
  }
  return next;
}
