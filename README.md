# AI × Commerce Digest

English | [中文](#中文说明)

---

A daily digest tracking top operators, founders, and builders at the intersection of AI and e-commerce — delivering curated, implementation-focused summaries of what they're shipping, testing, and learning.

**Philosophy:** Follow people who run stores, build tools, and share real numbers — not commentators who describe trends without doing the work.

## Quick Start

1. Clone into your Claude Code skills folder:
   ```bash
   git clone https://github.com/veraze/ecommerce-ai-digest-.git ~/.claude/skills/follow-builders
   cd ~/.claude/skills/follow-builders/scripts && npm install
   ```
2. Say **"set up follow builders"** to your agent
3. The agent walks you through setup — no config files to edit

Your first digest arrives immediately after setup.

## What You Get

A daily digest delivered to Telegram (or email) with:

- Key posts and tactics from 9 curated AI × e-commerce operators on X/Twitter
- Summaries of new episodes from 3 YouTube channels
- Links to all original content
- Available in English, Chinese, or bilingual

## Sources

### Operators & Builders on X (9)

| Name | Handle | Focus |
|------|--------|-------|
| Davie Fogarty | [@daviefogarty](https://x.com/daviefogarty) | Shopify $1B GMV, The Oodie founder, Shark Tank |
| Oliver Brocato | [@oliverbrocato](https://x.com/oliverbrocato) | Tabs Chocolate founder, now building brand-protection AI tool Bustem |
| Noah Frydberg | [@maverickecom](https://x.com/maverickecom) | TikTok Shop ops + AI UGC content systems |
| Chad Rubin | [@itschadrubin](https://x.com/itschadrubin) | 20-year D2C veteran, founder of AI pricing tool Profasee |
| Maxwell Finn | [@maxwellfinn](https://x.com/maxwellfinn) | TikTok Shop & Meta ads, DTC brand growth |
| Kurt Elster | [@kurtinc](https://x.com/kurtinc) | Shopify consultant, host of The Unofficial Shopify Podcast |
| Matthew Bertulli | [@mbertulli](https://x.com/mbertulli) | Co-host of Operators Podcast, founder of 4 companies |
| Tobi Lütke | [@tobi](https://x.com/tobi) | Shopify CEO — earliest signal on platform direction |
| Chris Lang | [@ChrisLangSocial](https://x.com/ChrisLangSocial) | Top 1% Shopify expert, CRO practitioner |

### YouTube Channels (3)

| Channel | Creator | Focus |
|---------|---------|-------|
| [@theecomacademy](https://www.youtube.com/@theecomacademy) | Brendan Gillen | Shopify growth tactics — ads, conversion, AI tools |
| [@DavieFogarty](https://www.youtube.com/@DavieFogarty) | Davie Fogarty | Behind-the-scenes of a $1B GMV brand — supply chain, marketing, AI |
| [@daanjonkman](https://www.youtube.com/@daanjonkman) | Daan Jonkman | AI for Shopify — workflows and tools for commerce |

## How It Works

1. GitHub Actions runs daily at 6am UTC — fetches tweets via Rettiwt (no API key needed) and YouTube transcripts via Supadata
2. Feed files (`feed-x.json`, `feed-podcasts.json`) are committed to this repo
3. Your agent fetches the feeds, remixes the content using your preferences
4. Delivered to Telegram, email, or shown in-chat

## Requirements

- An AI agent (Claude Code or similar)
- `SUPADATA_API_KEY` secret in your GitHub repo → Settings → Secrets (for YouTube transcripts — free at [supadata.ai](https://supadata.ai))
- No X/Twitter API key needed

## Changing Settings

Tell your agent:
- "Switch to weekly digests on Monday mornings"
- "Change language to Chinese"
- "Make summaries focus more on specific tactics and numbers"
- "Show me my current settings"

## Customizing Summaries

Edit the files in `prompts/`:
- `summarize-tweets.md` — how X posts are summarized
- `summarize-podcast.md` — how YouTube episodes are summarized
- `digest-intro.md` — overall format and tone
- `translate.md` — English → Chinese translation style

## License

MIT

---

# 中文说明

English | [中文](#中文说明)

---

每日追踪 AI × 电商领域顶尖操盘手、创始人和开发者，提炼他们正在测试、上线和总结的内容——聚焦具体实操，不讲泛泛趋势。

**核心理念：** 跟着真正在跑生意、做工具、晒数据的人学，而不是只会描述趋势却不动手的旁观者。

## 快速开始

1. 克隆到 Claude Code skills 目录：
   ```bash
   git clone https://github.com/veraze/ecommerce-ai-digest-.git ~/.claude/skills/follow-builders
   cd ~/.claude/skills/follow-builders/scripts && npm install
   ```
2. 对 agent 说 **"set up follow builders"**
3. Agent 会引导你完成所有配置，无需手动编辑文件

配置完成后立即发送第一条摘要。

## 你能收到什么

每日推送到 Telegram（或邮件）：

- 9 位精选 AI × 电商操盘手的 X/Twitter 最新动态与战术
- 3 个 YouTube 频道的最新视频摘要
- 所有原始内容链接
- 支持英文、中文或双语

## 信息源

### X 账号（9 个）

| 姓名 | 账号 | 方向 |
|------|------|------|
| Davie Fogarty | [@daviefogarty](https://x.com/daviefogarty) | Shopify 10 亿 GMV，The Oodie 创始人，Shark Tank |
| Oliver Brocato | [@oliverbrocato](https://x.com/oliverbrocato) | Tabs Chocolate 创始人，现做品牌保护 AI 工具 Bustem |
| Noah Frydberg | [@maverickecom](https://x.com/maverickecom) | TikTok Shop 实操 + AI UGC 内容系统 |
| Chad Rubin | [@itschadrubin](https://x.com/itschadrubin) | D2C 20 年老兵，AI 定价工具 Profasee 创始人 |
| Maxwell Finn | [@maxwellfinn](https://x.com/maxwellfinn) | TikTok Shop & Meta 广告投放，DTC 品牌增长 |
| Kurt Elster | [@kurtinc](https://x.com/kurtinc) | Shopify 顾问，The Unofficial Shopify Podcast 主持 |
| Matthew Bertulli | [@mbertulli](https://x.com/mbertulli) | Operators Podcast 联合主持，4 家公司创始人 |
| Tobi Lütke | [@tobi](https://x.com/tobi) | Shopify CEO，平台走向最早信号 |
| Chris Lang | [@ChrisLangSocial](https://x.com/ChrisLangSocial) | Top 1% Shopify 专家，CRO 实操 |

### YouTube 频道（3 个）

| 频道 | 创作者 | 方向 |
|------|--------|------|
| [@theecomacademy](https://www.youtube.com/@theecomacademy) | Brendan Gillen | Shopify 增长实操教学，广告、转化、AI 工具应用 |
| [@DavieFogarty](https://www.youtube.com/@DavieFogarty) | Davie Fogarty | 10 亿 GMV 品牌背后的实操复盘，供应链、营销、AI |
| [@daanjonkman](https://www.youtube.com/@daanjonkman) | Daan Jonkman | AI for Shopify — AI 工具与工作流，专注 Shopify 场景 |

## 工作原理

1. GitHub Actions 每天 UTC 早上 6 点自动运行，通过 Rettiwt（无需 API key）抓取推文，通过 Supadata 获取 YouTube 字幕
2. 生成的 feed 文件（`feed-x.json`、`feed-podcasts.json`）提交到本仓库
3. 你的 agent 读取 feed，按你的偏好生成摘要
4. 推送到 Telegram、邮件或直接在对话中显示

## 环境要求

- AI agent（Claude Code 或同类工具）
- 在 GitHub 仓库 Settings → Secrets 中添加 `SUPADATA_API_KEY`（免费注册：[supadata.ai](https://supadata.ai)）
- 无需 X/Twitter API key

## 修改设置

直接告诉你的 agent：
- "改成每周一早上推送"
- "切换成中文"
- "摘要更聚焦具体战术和数据"
- "显示我的当前设置"

## 自定义摘要风格

编辑 `prompts/` 目录下的文件：
- `summarize-tweets.md` — X 推文的摘要方式
- `summarize-podcast.md` — YouTube 视频的摘要方式
- `digest-intro.md` — 整体格式和语气
- `translate.md` — 英译中的风格

## 开源协议

MIT
