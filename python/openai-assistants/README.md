# OpenAI Assistants + Velixar

Give OpenAI function calling persistent memory. The AI decides when to store and recall.

## Setup

```bash
pip install velixar openai
export VELIXAR_API_KEY="vlx_your_key_here"
export OPENAI_API_KEY="sk-your_key_here"
```

## Run

```bash
python main.py
```

## What it does

1. Defines `remember` and `recall` as OpenAI function tools
2. The AI autonomously decides when to store facts and when to search memory
3. Run it twice — the second run recalls everything from the first
