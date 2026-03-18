// Vercel AI SDK + Velixar — streaming chat with persistent memory
import { openai } from "@ai-sdk/openai";
import { streamText } from "ai";
import { Velixar } from "velixar";

const v = new Velixar({ apiKey: process.env.VELIXAR_API_KEY! });

// Next.js App Router: app/api/chat/route.ts
export async function POST(req: Request) {
  const { messages } = await req.json();
  const lastMessage = messages[messages.length - 1].content;

  // Recall relevant memories
  const memories = await v.search(lastMessage, { limit: 3 });
  const context = memories.map((m) => `- ${m.content}`).join("\n") || "No prior context.";

  const result = streamText({
    model: openai("gpt-4o-mini"),
    system: `You have persistent memory of this user:\n${context}`,
    messages,
    async onFinish({ text }) {
      // Store the exchange after streaming completes
      await v.store(`User: ${lastMessage}\nAI: ${text}`, { tags: ["chat"] });
    },
  });

  return result.toDataStreamResponse();
}
