/**
 * ecommerce-ai-digest — Cloudflare Worker
 *
 * Serves the pre-built feed files (feed-x.json, feed-podcasts.json, feed-blogs.json)
 * from KV storage with CORS headers, so prepare-digest.js can fetch them without
 * hitting GitHub raw file rate limits.
 *
 * Routes:
 *   GET /feed/x            → feed-x.json
 *   GET /feed/podcasts     → feed-podcasts.json
 *   GET /feed/blogs        → feed-blogs.json
 *   GET /health            → { status: "ok", updatedAt: "..." }
 *
 * Deploy:
 *   1. wrangler kv:namespace create FEEDS
 *   2. Add the namespace ID to wrangler.toml (see below)
 *   3. wrangler deploy
 *
 * Feed files are written to KV by the GitHub Actions daily-feed.yml workflow
 * via the Cloudflare API after each successful generate-feed.js run.
 *
 * wrangler.toml example:
 * ─────────────────────────────────────────────
 * name = "ecommerce-ai-digest"
 * main = "server/worker.js"
 * compatibility_date = "2024-01-01"
 *
 * [[kv_namespaces]]
 * binding = "FEEDS"
 * id = "<your-kv-namespace-id>"
 * ─────────────────────────────────────────────
 */

const CORS_HEADERS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
};

const FEED_KEYS = {
  '/feed/x':        'feed-x',
  '/feed/podcasts': 'feed-podcasts',
  '/feed/blogs':    'feed-blogs',
};

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const path = url.pathname;

    // CORS preflight
    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: CORS_HEADERS });
    }

    // Health check
    if (path === '/health') {
      const updatedAt = await env.FEEDS.get('updated-at');
      return Response.json(
        { status: 'ok', updatedAt: updatedAt ?? null },
        { headers: CORS_HEADERS }
      );
    }

    // Feed routes
    const kvKey = FEED_KEYS[path];
    if (!kvKey) {
      return new Response(
        JSON.stringify({ error: 'Not found', routes: Object.keys(FEED_KEYS) }),
        { status: 404, headers: { 'Content-Type': 'application/json', ...CORS_HEADERS } }
      );
    }

    const value = await env.FEEDS.get(kvKey);
    if (!value) {
      return new Response(
        JSON.stringify({ error: 'Feed not yet generated. Check back after the next daily run.' }),
        { status: 503, headers: { 'Content-Type': 'application/json', ...CORS_HEADERS } }
      );
    }

    return new Response(value, {
      headers: {
        'Content-Type': 'application/json',
        'Cache-Control': 'public, max-age=3600', // 1 hour client cache
        ...CORS_HEADERS,
      },
    });
  },
};
