"use client";

import { useCallback, useEffect, useRef, useState } from "react";

import { AnswerCard } from "@/components/AnswerCard";
import { ConversationViewer } from "@/components/ConversationViewer";
import { SourcePanel } from "@/components/SourcePanel";
import { StepList } from "@/components/StepList";
import { ask, readEvents } from "@/lib/api";
import { applyEvent, type Run } from "@/lib/run";

const EXAMPLES = [
  "How long is a Delta account locked after too many failed logins?",
  "Why do songs disappear from Spotify playlists?",
  "What does UPS mean by end-of-day delivery?",
  "Can I bring my dog in the cabin on a Ryanair flight?",
];

export default function Home() {
  const [runs, setRuns] = useState<Run[]>([]);
  const [active, setActive] = useState<string | null>(null);
  const [question, setQuestion] = useState("");
  const [viewing, setViewing] = useState<number | null>(null);
  const abort = useRef<AbortController | null>(null);
  const bottom = useRef<HTMLDivElement>(null);
  const busy = runs.some((r) => r.status === "running");

  useEffect(() => bottom.current?.scrollIntoView({ behavior: "smooth" }), [runs]);

  const submit = useCallback(async (q: string) => {
    q = q.trim();
    if (q.length < 3) return;
    const key = crypto.randomUUID();
    const update = (f: (r: Run) => Run) => setRuns((rs) => rs.map((r) => (r.key === key ? f(r) : r)));
    setRuns((rs) => [...rs, { key, question: q, steps: [], hits: new Map(), status: "running" }]);
    setActive(key);
    setQuestion("");
    const ctrl = new AbortController();
    abort.current = ctrl;
    try {
      for await (const ev of readEvents(await ask(q, ctrl.signal))) update((r) => applyEvent(r, ev));
      update((r) => ({ ...r, status: r.answer ? "done" : "failed" }));
    } catch (e) {
      const reason = ctrl.signal.aborted ? "stopped by user" : (e as Error).message;
      update((r) => ({ ...r, status: "failed", steps: [...r.steps, { kind: "error", reason }] }));
    }
  }, []);

  const current = runs.find((r) => r.key === active) ?? runs.at(-1);
  const closeViewer = useCallback(() => setViewing(null), []);

  return (
    <div className="layout">
      <main className="chat">
        <header className="top">
          <h1>Support history Q&amp;A</h1>
          <p className="muted">
            Answers come only from ~800k customer-support conversations on Twitter (Oct–Dec 2017), and every answer
            is checked against the conversations it cites.
          </p>
        </header>

        {runs.length === 0 && (
          <div className="examples">
            {EXAMPLES.map((q) => (
              <button key={q} onClick={() => submit(q)}>
                {q}
              </button>
            ))}
          </div>
        )}

        {runs.map((r) => (
          <section key={r.key} className={`turn ${r.key === current?.key ? "active" : ""}`} onClick={() => setActive(r.key)}>
            <div className="question">{r.question}</div>
            <StepList steps={r.steps} running={r.status === "running"} />
            {r.answer && <AnswerCard answer={r.answer} usage={r.usage} onOpen={setViewing} />}
          </section>
        ))}
        <div ref={bottom} />

        <form
          className="composer"
          onSubmit={(e) => {
            e.preventDefault();
            submit(question);
          }}
        >
          <input
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="Ask about a company's support policies or fixes…"
            maxLength={1000}
            disabled={busy}
          />
          {busy ? (
            <button type="button" onClick={() => abort.current?.abort()}>
              Stop
            </button>
          ) : (
            <button type="submit" disabled={question.trim().length < 3}>
              Ask
            </button>
          )}
        </form>
      </main>

      <aside className="panel">
        <h2>Sources</h2>
        <SourcePanel
          hits={current ? [...current.hits.values()] : []}
          cited={new Set(current?.answer?.cited_conversation_ids ?? [])}
          onOpen={setViewing}
        />
      </aside>

      {viewing !== null && <ConversationViewer id={viewing} onClose={closeViewer} />}
    </div>
  );
}
