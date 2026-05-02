#!/usr/bin/env node
// format-digest.js — converts prepare-digest.js JSON output into readable digest text
// No LLM required. Works reliably in cron.
// Limits: max 5 tweets total (1 per builder, sorted by likes), max 2 podcasts.

const chunks = [];
for await (const chunk of process.stdin) chunks.push(chunk);
const raw = Buffer.concat(chunks).toString('utf-8').trim();
if (!raw) process.exit(0);

const data = JSON.parse(raw);
const lang = data.config?.language || 'en';
const bilingual = lang === 'bilingual';
const chinese = lang === 'zh';

const today = new Date().toLocaleDateString('zh-CN', {
  year: 'numeric', month: 'long', day: 'numeric',
  timeZone: 'Asia/Shanghai',
});

const lines = [];

// Header
if (bilingual || chinese) {
  lines.push(`🤖 AI × 电商每日简报 — ${today}`);
} else {
  lines.push(`🤖 AI × Commerce Digest — ${today}`);
}
lines.push('');

// ── X / Twitter ──────────────────────────────────────────────
// Pick best tweet per builder, sort by likes, take top 5
const xItems = data.x || [];
const topTweets = [];
for (const builder of xItems) {
  const tweets = builder.tweets || [];
  if (tweets.length === 0) continue;
  const best = tweets.reduce((a, b) => (b.likes || 0) > (a.likes || 0) ? b : a);
  topTweets.push({ builder, tweet: best });
}
topTweets.sort((a, b) => (b.tweet.likes || 0) - (a.tweet.likes || 0));
const selected = topTweets.slice(0, 5);

if (selected.length > 0) {
  if (bilingual || chinese) lines.push('━━━ X / 推特 ━━━');
  else lines.push('━━━ X / TWITTER ━━━');
  lines.push('');

  for (const { builder, tweet } of selected) {
    const name = builder.name || builder.handle;
    const text = tweet.text || '';
    const truncated = text.length > 300 ? text.slice(0, 297) + '...' : text;

    lines.push(`📌 ${name} @${builder.handle}`);
    lines.push('');
    lines.push(truncated);
    lines.push(tweet.url);
    lines.push('');
  }
}

// ── Podcasts / YouTube ────────────────────────────────────────
const podcasts = (data.podcasts || []).slice(0, 2);
if (podcasts.length > 0) {
  if (bilingual || chinese) lines.push('━━━ 播客 / YouTube ━━━');
  else lines.push('━━━ PODCASTS / YOUTUBE ━━━');
  lines.push('');

  for (const ep of podcasts) {
    lines.push(`🎙 ${ep.name}`);
    lines.push(`"${ep.title}"`);
    lines.push('');
    const transcript = ep.transcript || '';
    if (transcript) {
      const excerpt = transcript.slice(0, 300).replace(/\s+/g, ' ').trim();
      lines.push(excerpt + (transcript.length > 300 ? '...' : ''));
      lines.push('');
    }
    lines.push(ep.url);
    lines.push('');
  }
}

// Footer
lines.push('—');
lines.push('ecommerce-ai-digest: https://github.com/veraze/ecommerce-ai-digest-');

process.stdout.write(lines.join('\n'));
