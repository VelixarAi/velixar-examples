# FastAPI Chatbot with Velixar

REST API chatbot with per-user persistent memory. Every conversation is remembered.

## Setup

```bash
pip install velixar fastapi uvicorn openai
export VELIXAR_API_KEY="vlx_your_key_here"
export OPENAI_API_KEY="sk-your_key_here"
```

## Run

```bash
uvicorn main:app --reload
```

## Test

```bash
# Chat
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"user_id": "user_1", "message": "I prefer Python and dark mode"}'

# Chat again — it remembers
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"user_id": "user_1", "message": "What do you know about me?"}'

# List memories
curl http://localhost:8000/memories/user_1
```
