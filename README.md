# AI × Commerce Digest

A daily digest that tracks the top operators, founders, and builders at the intersection
of AI and e-commerce — and delivers curated, implementation-focused summaries of what
they're shipping, testing, and learning.

**Philosophy:** Follow people who run stores, build tools, and share real numbers —
not commentators who describe trends without doing the work.

## What You Get

A daily or weekly digest delivered to Telegram (or email) with:

- Key posts and tactics from 22 curated AI × e-commerce operators on X/Twitter
- Summaries of new episodes from top commerce and entrepreneurship podcasts
- Engineering posts from Shopify and other commerce infrastructure teams
- Links to all original content
- Available in English, Chinese, or bilingual

## Quick Start

1. Install in Claude Code:
   ```bash
   git clone https://github.com/veraze/ecommerce-ai-digest-.git ~/.claude/skills/follow-builders
   cd ~/.claude/skills/follow-builders/scripts && npm install
   ```
2. Say "set up follow builders" to your agent
3. The agent walks you through setup — no config files to edit

Your first digest arrives immediately after setup.

## Sources

### Operators & Builders on X (22)
| Name | Handle | Why |
|------|--------|-----|
| Tobi Lütke | tobi | Shopify CEO, ships AI into commerce infrastructure |
| Harley Finkelstein | harleyf | Shopify President, operator insights at scale |
| Nick Sharma | mrsharma | DTC investor, blunt takes on what actually works |
| Cody Plofker | codyplofker | CMO Jones Road Beauty, real paid + AI experiments |
| Taylor Holiday | taylorholiday | Common Thread Collective, DTC data and frameworks |
| Ezra Firestone | ezrafirestone | Smart Marketer, multi-brand e-comm operator |
| Kyle Hency | kylehency | Gorgias CEO, AI in e-commerce customer service |
| Andrew Youderian | youderian | eCommerceFuel founder, operator community |
| Chase Dimond | ecomchasedimond | Email marketing for e-commerce |
| Jason Goldberg | betashop | Commerce tech analyst |
| Moiz Ali | moizali | DTC brand founder, blunt operator takes |
| Rick Watson | rickatomerch | Commerce technology strategist |
| Eli Weiss | eliweiss | Retention/CX at Jones Road |
| Kunle Campbell | 2xecommerce | E-commerce operator and educator |
| Tracey Wallace | tracewall | Content & commerce strategy |
| Andrew Foxwell | andrewfoxwell | Paid social for e-commerce |
| Sam Parr | theSamParr | My First Million, business builder |
| Shaan Puri | ShaanVP | My First Million, business builder |
| Katelyn Bourgoin | KateBour | Consumer psychology and buying behavior |
| Matthew Holman | holman_matt | Subscription commerce |
| Sam Altman | sama | OpenAI CEO — AI capabilities that affect commerce |
| Shopify | Shopify | Official announcements and product launches |

### Podcasts (6)
- [My First Million](https://www.youtube.com/@MyFirstMillionPod) — business ideas, commerce, operator stories
- [eCommerceFuel](https://www.youtube.com/@eCommerceFuel) — DTC operator deep-dives
- [DTC Pod](https://www.youtube.com/@DTCPod) — brand building and growth
- [Operators](https://www.youtube.com/@OperatorsPodcast) — founders running real businesses
- [How I Built This](https://www.youtube.com/@HowIBuiltThis) — origin stories of commerce companies
- [Acquired](https://www.youtube.com/@AcquiredFM) — deep dives on companies that shaped commerce

### Blogs (2)
- [Shopify Engineering](https://shopify.engineering) — technical decisions at commerce scale
- [Shopify Blog](https://www.shopify.com/blog) — product and merchant updates

## How It Works

1. GitHub Actions runs `generate-feed.js` daily at 6am UTC, fetching tweets and podcast episodes
2. Feed files (`feed-x.json`, `feed-podcasts.json`, `feed-blogs.json`) are committed to this repo
3. Your agent fetches the feeds, remixes the content into a digest using your preferences
4. The digest is delivered to Telegram, email, or shown in-chat

Optionally, you can deploy the included Cloudflare Worker (`server/worker.js`) to serve
feeds via KV storage instead of GitHub raw files — faster and no rate limit concerns.

## Requirements

- An AI agent (Claude Code or similar)
- `X_BEARER_TOKEN` secret in your GitHub repo → Settings → Secrets (for tweet fetching)
- Internet connection

> **Note on X API:** The feed generator uses the official X API v2 with a Bearer Token.
> You need a free X Developer account at [developer.x.com](https://developer.x.com).
> The free tier allows fetching recent tweets, which is all this tool needs.

## Changing Settings

Tell your agent:
- "Switch to weekly digests on Monday mornings"
- "Change language to Chinese"
- "Make the summaries focus more on specific tactics and numbers"
- "Show me my current settings"

## Customizing Summaries

Edit the files in `prompts/`:
- `summarize-tweets.md` — how X/Twitter posts are summarized
- `summarize-podcast.md` — how podcast episodes are summarized
- `summarize-blogs.md` — how blog posts are summarized
- `digest-intro.md` — overall format and tone
- `translate.md` — English → Chinese translation style

These are plain English instructions. Changes take effect on the next digest.

## Cloudflare Worker (Optional)

For faster feed delivery without GitHub raw file latency:

```bash
npm install -g wrangler
wrangler kv:namespace create FEEDS
# Add the namespace ID to wrangler.toml
wrangler deploy
```

Then uncomment the KV push step in `.github/workflows/daily-feed.yml` and add
`CLOUDFLARE_API_TOKEN`, `CLOUDFLARE_ACCOUNT_ID`, and `CLOUDFLARE_KV_NAMESPACE_ID`
as GitHub secrets.

## License

MIT
