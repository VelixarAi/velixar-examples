# LangChain + Velixar

Persistent memory backend for any LangChain chain. Memories survive across sessions — restart the script and your AI still remembers.

## Setup

```bash
pip install velixar langchain langchain-openai
export VELIXAR_API_KEY="vlx_your_key_here"
export OPENAI_API_KEY="sk-your_key_here"
```

## Run

```bash
python main.py
```

## What it does

1. Creates a `VelixarMemory` class implementing LangChain's `BaseMemory`
2. On each turn: searches Velixar for relevant context, injects into prompt
3. After each turn: stores the exchange as a memory
4. Run it twice — the second run remembers everything from the first
