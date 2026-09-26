import type { Answer, Usage } from "@/lib/api";

const CITE = /\[#(\d+)\]/g;

function withCitations(text: string, onOpen: (id: number) => void) {
  const parts: React.ReactNode[] = [];
  let last = 0;
  for (const m of text.matchAll(CITE)) {
    parts.push(text.slice(last, m.index));
    const id = Number(m[1]);
    parts.push(
      <button key={`${m.index}-${id}`} className="cite" onClick={() => onOpen(id)} title={`Open conversation #${id}`}>
        #{id}
      </button>,
    );
    last = (m.index ?? 0) + m[0].length;
  }
  parts.push(text.slice(last));
  return parts;
}

export function AnswerCard({ answer, usage, onOpen }: { answer: Answer; usage?: Usage; onOpen: (id: number) => void }) {
  const badge = !answer.answerable
    ? { cls: "none", text: "Not in the support history" }
    : answer.verified
      ? { cls: "ok", text: "Verified against sources" }
      : { cls: "bad", text: "Could not fully verify" };
  return (
    <div className="answer">
      <span className={`badge ${badge.cls}`}>{badge.text}</span>
      <div className="answer-text">{withCitations(answer.answer, onOpen)}</div>
      {!answer.verified && answer.verification.unsupported_claims.length > 0 && (
        <div className="warn">
          Unsupported: {answer.verification.unsupported_claims.join("; ")}
        </div>
      )}
      {usage && (
        <div className="usage">
          {usage.model_calls} model calls · {(usage.input_tokens + usage.cache_read_tokens).toLocaleString()} in /{" "}
          {usage.output_tokens.toLocaleString()} out tokens · ${usage.cost_usd.toFixed(3)} · {usage.latency_s}s
        </div>
      )}
    </div>
  );
}
