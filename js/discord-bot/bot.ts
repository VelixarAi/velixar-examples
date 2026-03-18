// Discord bot that remembers users across conversations
import { Client, GatewayIntentBits } from "discord.js";
import { Velixar } from "velixar";
import OpenAI from "openai";

const v = new Velixar({ apiKey: process.env.VELIXAR_API_KEY! });
const oai = new OpenAI();
const client = new Client({
  intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages, GatewayIntentBits.MessageContent],
});

const PREFIX = "!ask ";

client.on("messageCreate", async (msg) => {
  if (msg.author.bot || !msg.content.startsWith(PREFIX)) return;
  const question = msg.content.slice(PREFIX.length);
  const userId = msg.author.id;

  // Recall memories for this user
  const memories = await v.search(question, { limit: 3 });
  const context = memories.map((m) => `- ${m.content}`).join("\n") || "No prior context.";

  const completion = await oai.chat.completions.create({
    model: "gpt-4o-mini",
    messages: [
      { role: "system", content: `You're a helpful Discord bot with memory.\nUser memories:\n${context}` },
      { role: "user", content: question },
    ],
  });
  const answer = completion.choices[0].message.content!;

  // Store exchange tagged to this Discord user
  await v.store(`${msg.author.username}: ${question}\nBot: ${answer}`, {
    tags: [`discord:${userId}`, "chat"],
  });

  msg.reply(answer);
});

client.login(process.env.DISCORD_TOKEN);
