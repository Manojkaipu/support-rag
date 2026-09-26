import type { Hit } from "@/lib/api";

export function SourcePanel({
  hits,
  cited,
  onOpen,
}: {
  hits: Hit[];
  cited: Set<number>;
  onOpen: (id: number) => void;
}) {
  if (!hits.length) return <p className="muted">Retrieved conversations show up here.</p>;
  const sorted = [...hits].sort((a, b) => Number(cited.has(b.conversation_id)) - Number(cited.has(a.conversation_id)));
  return (
    <ul className="sources">
      {sorted.map((h) => (
        <li key={h.conversation_id} className={cited.has(h.conversation_id) ? "cited" : ""}>
          <button onClick={() => onOpen(h.conversation_id)}>
            <div className="source-head">
              <span>#{h.conversation_id}</span>
              <span className="tag">{h.company}</span>
              <span className="muted">{h.date}</span>
              {cited.has(h.conversation_id) && <span className="badge ok">cited</span>}
            </div>
            <div className="snippet">{h.snippet.slice(0, 280)}</div>
          </button>
        </li>
      ))}
    </ul>
  );
}
