/** @type {import('next').NextConfig} */
const nextConfig = {
  output: "standalone",
  env: {
    NEXT_PUBLIC_API_URL: process.env.NEXT_PUBLIC_API_URL || "https://to-do-app-hackathon-2-production.up.railway.app",
  },
};

module.exports = nextConfig;
