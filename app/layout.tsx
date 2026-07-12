import type { Metadata } from "next";
import Link from "next/link";

import "./globals.css";

export const metadata: Metadata = {
  title: "Finance Learning Graph",
  description: "Minimal reading app over the canonical finance knowledge graph",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <header className="site-header">
          <Link href="/" className="site-title">
            Finance Learning Graph
          </Link>
          <nav>
            <Link href="/">Modules</Link>
            <Link href="/learn">Learn</Link>
          </nav>
        </header>
        <main className="container">{children}</main>
        <footer className="site-footer">
          <p>Milestone 4 — canonical JSON proof-of-concept. No auth, no database.</p>
        </footer>
      </body>
    </html>
  );
}
