// Proxies /api/* to the backend so the browser only talks to this origin and the
// backend address is a runtime setting (API_URL), not baked into the bundle.
// Response bodies are passed through unbuffered, which keeps SSE streaming.

const API_URL = process.env.API_URL ?? "http://localhost:8000";

export const dynamic = "force-dynamic";

async function proxy(req: Request, { params }: { params: Promise<{ path: string[] }> }) {
  const { path } = await params;
  const url = new URL(req.url);
  const target = `${API_URL}/api/${path.map(encodeURIComponent).join("/")}${url.search}`;
  const upstream = await fetch(target, {
    method: req.method,
    headers: { "content-type": req.headers.get("content-type") ?? "application/json" },
    body: req.method === "GET" ? undefined : await req.text(),
    signal: req.signal, // client disconnect cancels the agent run upstream
  });
  const headers = new Headers({ "content-type": upstream.headers.get("content-type") ?? "application/json" });
  if (headers.get("content-type")?.startsWith("text/event-stream")) {
    headers.set("cache-control", "no-cache");
    headers.set("x-accel-buffering", "no");
  }
  return new Response(upstream.body, { status: upstream.status, headers });
}

export { proxy as GET, proxy as POST };
