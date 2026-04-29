**English** | [中文](README.zh-CN.md)

# Follow AI × e-Commerce founders 

An AI-powered digest that tracks top founders, and builders at the intersection
of AI and e-commerce — people running real stores, shipping commerce tools, and sharing
what actually works — and delivers curated, implementation-focused summaries of what
they're testing and learning.

**Philosophy:**  Follow the people actually doing it, not talking about it.

## What You Get

A daily or weekly digest delivered to your preferred messaging app (Telegram, email,
etc.) with:

- Key posts and tactics from 9 curated AI × e-commerce operators on X/Twitter
- Summaries of new episodes from 3 YouTube channels focused on Shopify and AI commerce
- Links to all original content
- Available in English, Chinese, or bilingual

## Quick Start

1. Install the skill in your agent (Claude Code or similar):
   ```bash
   git clone https://github.com/veraze/ecommerce-ai-digest-.git ~/.claude/skills/follow-builders
   cd ~/.claude/skills/follow-builders/scripts && npm install
   ```
2. Say **"set up follow builders"** to your agent
3. The agent walks you through setup conversationally — no config files to edit

The agent will ask you:
- How often you want your digest (daily or weekly) and what time
- What language you prefer
- How you want it delivered (Telegram, email, or in-chat)

Your first digest arrives immediately after setup.

## Changing Settings

Your delivery preferences are configurable through conversation. Just tell your agent:

- "Switch to weekly digests on Monday mornings"
- "Change language to Chinese"
- "Make the summaries focus more on specific tactics and numbers"
- "Show me my current settings"

The source list is curated centrally and updates automatically — you always get the
latest sources without doing anything.

## Customizing the Summaries

The skill uses plain-English prompt files to control how content is summarized.
You can customize them two ways:

**Through conversation (recommended):**
Tell your agent what you want — "Make summaries more concise," "Focus on actionable
tactics with real numbers," "Use a more casual tone." The agent updates the prompts for you.

**Direct editing (power users):**
Edit the files in the `prompts/` folder:
- `summarize-podcast.md` — how YouTube episodes are summarized
- `summarize-tweets.md` — how X/Twitter posts are summarized
- `digest-intro.md` — the overall digest format and tone
- `translate.md` — how English content is translated to Chinese

These are plain English instructions, not code. Changes take effect on the next digest.

## Default Sources

### YouTube Channels (3)
- [The Ecom Academy](https://www.youtube.com/@theecomacademy) — Shopify growth tactics: ads, conversion, AI tools (Brendan Gillen)
- [Davie Fogarty](https://www.youtube.com/@DavieFogarty) — Behind the scenes of a $1B GMV brand: supply chain, marketing, AI
- [Daan Jonkman](https://www.youtube.com/@daanjonkman) — AI for Shopify: workflows and tools for commerce operators

### AI × Commerce Operators on X (9)
[Davie Fogarty](https://x.com/daviefogarty), [Oliver Brocato](https://x.com/oliverbrocato), [Noah Frydberg](https://x.com/maverickecom), [Chad Rubin](https://x.com/itschadrubin), [Maxwell Finn](https://x.com/maxwellfinn), [Kurt Elster](https://x.com/kurtinc), [Matthew Bertulli](https://x.com/mbertulli), [Tobi Lütke](https://x.com/tobi), [Chris Lang](https://x.com/ChrisLangSocial)

## Installation

### Claude Code
```bash
git clone https://github.com/veraze/ecommerce-ai-digest-.git ~/.claude/skills/follow-builders
cd ~/.claude/skills/follow-builders/scripts && npm install
```

## Requirements

- An AI agent (Claude Code or similar)
- Internet connection (to fetch the central feed)
- `SUPADATA_API_KEY` in your GitHub repo Secrets (for YouTube transcripts — free at [supadata.ai](https://supadata.ai))

No X/Twitter API key needed — tweets are fetched via Rettiwt guest mode.

## How It Works

1. A GitHub Actions workflow runs daily at 6am UTC, fetching tweets via Rettiwt (no API key)
   and YouTube transcripts via Supadata
2. Feed files (`feed-x.json`, `feed-podcasts.json`) are committed to this repo
3. Your agent fetches the feeds — one HTTP request
4. Your agent remixes the raw content into a digest using your preferences
5. The digest is delivered to your messaging app (or shown in-chat)

## Privacy

- No API keys are sent anywhere — all content is fetched centrally
- If you use Telegram/email delivery, those keys are stored locally in `~/.follow-builders/.env`
- The skill only reads public content (public YouTube videos, public X posts)
- Your configuration, preferences, and reading history stay on your machine
- Inspired by and forked from @zarazhangrui

## License

MIT
