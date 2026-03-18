# Next.js + Velixar

API route that gives your Next.js app per-user persistent memory.

## Setup

```bash
npm install velixar openai
```

Set environment variables in `.env.local`:
```
VELIXAR_API_KEY=vlx_your_key_here
OPENAI_API_KEY=sk-your_key_here
```

## Usage

Copy `pages/api/chat.ts` into your Next.js project and call it:

```ts
const res = await fetch("/api/chat", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ message: "I prefer dark mode", userId: "user_1" }),
});
```
