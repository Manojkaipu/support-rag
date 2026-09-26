"use client";

import { useEffect, useState } from "react";

import { getConversation, type Conversation } from "@/lib/api";

export function ConversationViewer({ id, onClose }: { id: number; onClose: () => void }) {
  const [conv, setConv] = useState<Conversation | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setConv(null);
    setError(null);
    getConversation(id).then(setConv, (e: Error) => setError(e.message));
  }, [id]);

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => e.key === "Escape" && onClose();
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [onClose]);

  return (
    <div className="overlay" onClick={onClose}>
      <div className="viewer" onClick={(e) => e.stopPropagation()} role="dialog" aria-label={`Conversation ${id}`}>
        <header>
          <strong>Conversation #{id}</strong>
          {conv && (
            <span className="muted">
              {" "}
              · {conv.company} · {new Date(conv.started_at).toLocaleDateString()}
            </span>
          )}
          <button className="close" onClick={onClose} aria-label="Close">
            ×
          </button>
        </header>
        {error && <p className="warn">{error}</p>}
        {!conv && !error && <p className="muted">Loading…</p>}
        {conv && (
          <div className="thread">
            {conv.tweets.map((t) => (
              <div key={t.turn} className={`bubble ${t.inbound ? "customer" : "company"}`}>
                <div className="who">
                  {t.inbound ? "Customer" : t.author} · {new Date(t.created_at).toLocaleString()}
                </div>
                {t.text}
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
