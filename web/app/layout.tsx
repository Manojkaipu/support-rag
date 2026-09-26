import type { Metadata } from "next";

import "./globals.css";

export const metadata: Metadata = {
  title: "Support history Q&A",
  description: "Agentic question answering over customer-support conversations",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
