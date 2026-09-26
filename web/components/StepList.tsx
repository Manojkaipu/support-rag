import type { Step } from "@/lib/run";

function StepRow({ step }: { step: Step }) {
  switch (step.kind) {
    case "thinking":
      return (
        <details className="step thinking">
          <summary>Thinking</summary>
          <p>{step.text}</p>
        </details>
      );
    case "text":
      return <div className="step plan">{step.text}</div>;
    case "search":
      return (
        <div className="step tool">
          <span className="label">Search</span> “{step.query}”
          {step.company !== "any" && <span className="tag">{step.company}</span>}
          <span className="muted">
            {step.error ? ` · ${step.error}` : step.hits ? ` · ${step.hits.length} conversations` : " · …"}
          </span>
        </div>
      );
    case "open":
      return (
        <div className="step tool">
          <span className="label">Read</span> conversation #{step.conversationId}
          <span className="muted">
            {step.error ? ` · ${step.error}` : step.turns ? ` · ${step.company}, ${step.turns} turns` : " · …"}
          </span>
        </div>
      );
    case "submit":
      return (
        <div className="step tool">
          <span className="label">Submit</span> draft answer
        </div>
      );
    case "verify":
      return (
        <div className={`step verify ${step.supported ? "ok" : "bad"}`}>
          <span className="label">Check #{step.attempt}</span>
          {step.supported ? "every claim is supported by a cited conversation" : "unsupported claims:"}
          {!step.supported && (
            <ul>
              {step.claims.map((c, i) => (
                <li key={i}>{c}</li>
              ))}
            </ul>
          )}
        </div>
      );
    case "error":
      return <div className="step verify bad">Stopped: {step.reason}</div>;
  }
}

export function StepList({ steps, running }: { steps: Step[]; running: boolean }) {
  return (
    <div className="steps">
      {steps.map((s, i) => (
        <StepRow key={i} step={s} />
      ))}
      {running && <div className="step muted pulse">working…</div>}
    </div>
  );
}
