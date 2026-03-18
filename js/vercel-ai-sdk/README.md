# Vercel AI SDK + Velixar

Streaming chat with persistent memory using the Vercel AI SDK.

## Setup

```bash
npm install velixar ai @ai-sdk/openai
```

## Usage

Drop `route.ts` into `app/api/chat/route.ts` in your Next.js app. Pair with the `useChat` hook on the frontend:

```tsx
"use client";
import { useChat } from "ai/react";

export default function Chat() {
  const { messages, input, handleInputChange, handleSubmit } = useChat();
  return (
    <div>
      {messages.map((m) => <div key={m.id}>{m.role}: {m.content}</div>)}
      <form onSubmit={handleSubmit}>
        <input value={input} onChange={handleInputChange} />
      </form>
    </div>
  );
}
```

Every conversation is stored in Velixar. Refresh the page, come back tomorrow — the AI still remembers.
