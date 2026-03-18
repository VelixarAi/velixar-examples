# Discord Bot + Velixar

A Discord bot that remembers every user across conversations.

## Setup

```bash
npm install velixar openai discord.js
```

Set environment variables:
```
VELIXAR_API_KEY=vlx_your_key_here
OPENAI_API_KEY=sk-your_key_here
DISCORD_TOKEN=your_discord_bot_token
```

## Run

```bash
npx tsx bot.ts
```

## Usage

In any Discord channel the bot is in:
```
!ask What's the best way to learn Rust?
!ask Remember that I'm interested in systems programming
!ask What do you know about me?
```

The bot remembers each user separately via Velixar tags.
