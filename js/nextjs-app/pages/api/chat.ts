// Next.js API route — per-user AI memory
// pages/api/chat.ts (or app/api/chat/route.ts)
import { Velixar } from "velixar";
import OpenAI from "openai";
import type { NextApiRequest, NextApiResponse } from "next";

const v = new Velixar({ apiKey: process.env.VELIXAR_API_KEY! });
const oai = new OpenAI();

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  const { message, userId } = req.body;

  // Recall relevant context
  const memories = await v.search(message, { limit: 3 });
  const context = memories.map((m) => `- ${m.content}`).join("\n") || "No prior context.";

  // Generate response with memory
  const completion = await oai.chat.completions.create({
    model: "gpt-4o-mini",
    messages: [
      { role: "system", content: `You have memory of this user:\n${context}` },
      { role: "user", content: message },
    ],
  });
  const answer = completion.choices[0].message.content;

  // Store exchange
  await v.store(`User: ${message}\nAI: ${answer}`, { tags: [`user:${userId}`, "chat"] });

  res.json({ response: answer, memoriesUsed: memories.length });
}
