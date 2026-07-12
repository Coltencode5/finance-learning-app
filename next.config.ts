import path from "node:path";
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  reactStrictMode: true,
  // Keep file tracing rooted at this app (parent home lockfile confuses inference).
  outputFileTracingRoot: path.join(__dirname),
};

export default nextConfig;
