// Same-origin: app/api/[...path]/route.ts forwards to the backend.
export const API = "";

export type Hit = {
  conversation_id: number;
  chunk_id: number;
  score: number;
  company: string;
  date: string;
  snippet: string;
};

export type Verdict = {
  supported: boolean;
  unsupported_claims: string[];
  feedback: string;
};

export type Answer = {
  answer: string;
  cited_conversation_ids: number[];
  answerable: boolean;
  verified: boolean;
  verification: Verdict;
};

export type Usage = {
  input_tokens: number;
  output_tokens: number;
  cache_read_tokens: number;
  cache_write_tokens: number;
  cost_usd: number;
  model_calls: number;
  latency_s: number;
};

export type AgentEvent =
  | { type: "run"; data: { run_id: string } }
  | { type: "thinking" | "text"; data: { text: string } }
  | { type: "tool_call"; data: { id: string; name: string; input: Record<string, unknown> } }
  | {
      type: "tool_result";
      data: { id: string; name: string; hits?: Hit[]; conversation_id?: number; company?: string; turns?: number; error?: string };
    }
  | { type: "verification"; data: Verdict & { attempt: number } }
  | { type: "answer"; data: Answer }
  | { type: "usage"; data: Usage }
  | { type: "error"; data: { reason: string } };

export type Tweet = { turn: number; author: string; inbound: boolean; created_at: string; text: string };
export type Conversation = { id: number; company: string; started_at: string; n_turns: number; tweets: Tweet[] };

/** Parses a text/event-stream body into events as they arrive. */
export async function* readEvents(body: ReadableStream<Uint8Array>): AsyncGenerator<AgentEvent> {
  const reader = body.getReader();
  const decoder = new TextDecoder();
  let buf = "";
  for (;;) {
    const { value, done } = await reader.read();
    if (done) break;
    buf += decoder.decode(value, { stream: true });
    let end;
    while ((end = buf.indexOf("\n\n")) >= 0) {
      const block = buf.slice(0, end);
      buf = buf.slice(end + 2);
      let type = "message";
      const data: string[] = [];
      for (const line of block.split("\n")) {
        if (line.startsWith("event: ")) type = line.slice(7);
        else if (line.startsWith("data: ")) data.push(line.slice(6));
      }
      if (data.length) yield { type, data: JSON.parse(data.join("\n")) } as AgentEvent;
    }
  }
}

export async function ask(question: string, signal: AbortSignal): Promise<ReadableStream<Uint8Array>> {
  const res = await fetch(`${API}/api/ask`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question }),
    signal,
  });
  if (!res.ok || !res.body) throw new Error(`request failed (${res.status})`);
  return res.body;
}

export async function getConversation(id: number): Promise<Conversation> {
  const res = await fetch(`${API}/api/conversations/${id}`);
  if (!res.ok) throw new Error(`conversation ${id} not found`);
  return res.json();
}
