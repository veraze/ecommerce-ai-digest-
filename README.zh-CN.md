[English](README.md) | **中文**

# 追踪 AI × 电商操盘手

一个 AI 驱动的信息聚合工具，追踪 AI × 电商领域最顶尖的操盘手、创始人和工具开发者——真正在跑店铺、做产品、晒数据的人——并将他们的最新动态整理成聚焦实操的摘要推送给你。

**理念：** 追踪那些真正在跑生意、做工具、分享真实数据的人，而非只会描述趋势却不动手的旁观者。

## 你会得到什么

每日或每周推送到你常用的通讯工具（Telegram、邮件等），包含：

- 9 位精选 AI × 电商操盘手在 X/Twitter 上的关键动态和战术
- 3 个聚焦 Shopify 与 AI 电商的 YouTube 频道最新视频摘要
- 所有原始内容的链接
- 支持英文、中文或双语版本

## 快速开始

1. 在你的 AI agent 中安装此 skill（Claude Code 或类似工具）：
   ```bash
   git clone https://github.com/veraze/ecommerce-ai-digest-.git ~/.claude/skills/follow-builders
   cd ~/.claude/skills/follow-builders/scripts && npm install
   ```
2. 对 agent 说 **"set up follow builders"**
3. Agent 会以对话方式引导你完成设置——不需要手动编辑任何配置文件

Agent 会询问你：
- 推送频率（每日或每周）和时间
- 语言偏好
- 推送方式（Telegram、邮件或直接在聊天中显示）

设置完成后，你的第一期摘要会立即推送。

## 修改设置

通过对话即可修改推送偏好。直接告诉你的 agent：

- "改成每周一早上推送"
- "语言换成中文"
- "摘要更聚焦具体战术和真实数据"
- "显示我当前的设置"

信息源列表由中心化统一管理和更新——你无需做任何操作即可获得最新的信息源。

## 自定义摘要风格

Skill 使用纯文本 prompt 文件来控制内容的摘要方式。你可以通过两种方式自定义：

**通过对话（推荐）：**
直接告诉你的 agent——"摘要写得更简练一些"、"多关注可落地的战术和具体数字"、"用更轻松的语气"。Agent 会自动帮你更新 prompt。

**直接编辑（高级用户）：**
编辑 `prompts/` 文件夹中的文件：
- `summarize-podcast.md` — YouTube 视频的摘要方式
- `summarize-tweets.md` — X/Twitter 帖子的摘要方式
- `digest-intro.md` — 整体摘要的格式和语气
- `translate.md` — 英文内容翻译为中文的方式

这些都是纯文本指令，不是代码。修改后下次推送即生效。

## 默认信息源

### YouTube 频道（3个）
- [The Ecom Academy](https://www.youtube.com/@theecomacademy) — Shopify 增长实操教学：广告、转化、AI 工具应用（Brendan Gillen）
- [Davie Fogarty](https://www.youtube.com/@DavieFogarty) — 10 亿 GMV 品牌背后的实操复盘：供应链、营销、AI
- [Daan Jonkman](https://www.youtube.com/@daanjonkman) — AI for Shopify：AI 工具与工作流，专注电商场景

### X 上的 AI × 电商操盘手（9位）
[Davie Fogarty](https://x.com/daviefogarty), [Oliver Brocato](https://x.com/oliverbrocato), [Noah Frydberg](https://x.com/maverickecom), [Chad Rubin](https://x.com/itschadrubin), [Maxwell Finn](https://x.com/maxwellfinn), [Kurt Elster](https://x.com/kurtinc), [Matthew Bertulli](https://x.com/mbertulli), [Tobi Lütke](https://x.com/tobi), [Chris Lang](https://x.com/ChrisLangSocial)

## 安装

### Claude Code
```bash
git clone https://github.com/veraze/ecommerce-ai-digest-.git ~/.claude/skills/follow-builders
cd ~/.claude/skills/follow-builders/scripts && npm install
```

## 系统要求

- 一个 AI agent（Claude Code 或类似工具）
- 网络连接（用于获取 feed）
不需要额外的API KEY

## 工作原理

1. GitHub Actions 每天 UTC 早上 6 点自动运行，通过 Rettiwt（无需 API key）抓取推文，通过 Supadata 获取 YouTube 字幕
2. 生成的 feed 文件（`feed-x.json`、`feed-podcasts.json`）提交到本仓库
3. 你的 agent 获取 feed——一次 HTTP 请求
4. 你的 agent 根据你的偏好将原始内容重新混编为摘要
5. 摘要推送到你的通讯工具（或直接在聊天中显示）

## 隐私

- 不发送任何 API key——所有内容由中心化服务获取
- 如果你使用 Telegram/邮件推送，相关 key 仅存储在本地 `~/.follow-builders/.env`
- Skill 只读取公开内容（公开的 YouTube 视频和 X 帖子）
- 你的配置、偏好和阅读记录都保留在你自己的设备上

## 许可证

MIT
