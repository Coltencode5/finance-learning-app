import type { Metadata } from "next";
import Link from "next/link";

import "./globals.css";

export const metadata: Metadata = {
  title: {
    default: "Finance Learning",
    template: "%s — Finance Learning",
  },
  description:
    "Structured finance education — learn core concepts one screen at a time.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <header className="site-header">
          <Link href="/" className="site-title">
            Finance Learning
          </Link>
          <nav aria-label="Main">
            <Link href="/learn">Learn</Link>
            <Link href="/">Topics</Link>
          </nav>
        </header>
        <main className="container">{children}</main>
        <footer className="site-footer">
          <p>Structured finance education for curious learners.</p>
        </footer>
      </body>
    </html>
  );
}
