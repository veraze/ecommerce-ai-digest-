#!/usr/bin/env node
// format-digest.js — converts prepare-digest.js JSON output into readable digest text
// No LLM required. Works reliably in cron.

import { readFileSync } from 'fs';

const chunks = [];
for await (const chunk of process.stdin) chunks.push(chunk);
const raw = Buffer.concat(chunks).toString('utf-8').trim();
if (!raw) process.exit(0);

const data = JSON.parse(raw);
const lang = data.config?.language || 'en';
const bilingual = lang === 'bilingual';
const chinese = lang === 'zh';

const today = new Date().toLocaleDateString('en-US', {
  year: 'numeric', month: 'long', day: 'numeric'
});

const lines = [];

// Header
if (bilingual) {
  lines.push(`AI × Commerce Digest — ${today}`);
  lines.push(`AI × 电商每日简报 — ${today}`);
} else if (chinese) {
  lines.push(`AI × 电商每日简报 — ${today}`);
} else {
  lines.push(`AI × Commerce Digest — ${today}`);
}
lines.push('');

// ── X / Twitter ──────────────────────────────────────────────
const xItems = data.x || [];
if (xItems.length > 0) {
  if (bilingual) lines.push('━━━ X / TWITTER ━━━');
  else if (chinese) lines.push('━━━ X / 推特 ━━━');
  else lines.push('━━━ X / TWITTER ━━━');
  lines.push('');

  for (const builder of xItems) {
    const name = builder.name || builder.handle;
    const bio = builder.bio || '';
    const bioSnippet = bio.length > 80 ? bio.slice(0, 77) + '...' : bio;

    lines.push(`${name}`);
    if (bioSnippet) lines.push(`${bioSnippet}`);
    lines.push('');

    for (const tweet of builder.tweets || []) {
      const text = tweet.text || '';
      const truncated = text.length > 280 ? text.slice(0, 277) + '...' : text;
      lines.push(truncated);
      lines.push(tweet.url);
      lines.push('');
    }
  }
}

// ── Podcasts ──────────────────────────────────────────────────
const podcasts = data.podcasts || [];
if (podcasts.length > 0) {
  if (bilingual) lines.push('━━━ PODCASTS ━━━');
  else if (chinese) lines.push('━━━ 播客 ━━━');
  else lines.push('━━━ PODCASTS ━━━');
  lines.push('');

  for (const ep of podcasts) {
    lines.push(`${ep.name} — "${ep.title}"`);
    lines.push('');

    // Extract a short excerpt from transcript (first ~400 chars of content)
    const transcript = ep.transcript || '';
    if (transcript) {
      const excerpt = transcript.slice(0, 400).replace(/\s+/g, ' ').trim();
      lines.push(excerpt + (transcript.length > 400 ? '...' : ''));
      lines.push('');
    }

    lines.push(ep.url);
    lines.push('');
  }
}

// Footer
lines.push('Generated via ecommerce-ai-digest: https://github.com/veraze/ecommerce-ai-digest-');

process.stdout.write(lines.join('\n'));
