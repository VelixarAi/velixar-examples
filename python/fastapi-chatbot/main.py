# FastAPI Chatbot with Velixar — per-user persistent memory
import os
from fastapi import FastAPI
from pydantic import BaseModel
from velixar import Velixar
from openai import OpenAI

app = FastAPI()
v = Velixar(api_key=os.environ["VELIXAR_API_KEY"])
oai = OpenAI()


class ChatRequest(BaseModel):
    user_id: str
    message: str


@app.post("/chat")
async def chat(req: ChatRequest):
    # Recall relevant context for this user
    memories = v.search(req.message, limit=3)
    context = "\n".join(f"- {m.content}" for m in memories) or "No prior context."

    # Generate response with memory context
    resp = oai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"You have memory of this user:\n{context}"},
            {"role": "user", "content": req.message},
        ],
    )
    answer = resp.choices[0].message.content

    # Store the exchange for future recall
    v.store(f"User: {req.message}\nAI: {answer}", tags=[f"user:{req.user_id}", "chat"])
    return {"response": answer, "memories_used": len(memories)}


@app.get("/memories/{user_id}")
async def list_memories(user_id: str):
    memories = v.list(limit=20)
    return {"memories": [{"id": m.id, "content": m.content, "tags": m.tags} for m in memories]}
