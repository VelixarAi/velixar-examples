# Velixar Examples

Copy-paste examples for adding persistent AI memory to any application. Each example is standalone and runs in under 2 minutes.

## What is Velixar?

Velixar is cognitive memory infrastructure for AI. Your AI remembers users, tracks how they evolve, and detects contradictions — across every session. [Learn more →](https://docs.velixarai.com)

## Get Your API Key

1. Sign up free at [velixarai.com](https://velixarai.com)
2. Go to **Settings → API Keys**
3. Copy your key and set it:

```bash
export VELIXAR_API_KEY="vlx_your_key_here"
```

## Examples

### Python

| Example | Description | Complexity |
|---------|-------------|------------|
| [Quickstart](python/quickstart/) | Store and search memories in 10 lines | ⭐ |
| [LangChain Memory](python/langchain-memory/) | Persistent memory backend for any LangChain chain | ⭐⭐ |
| [CrewAI Agents](python/crewai-agents/) | Multi-agent system with shared memory | ⭐⭐ |
| [FastAPI Chatbot](python/fastapi-chatbot/) | REST API chatbot with per-user memory | ⭐⭐ |
| [OpenAI Assistants](python/openai-assistants/) | Assistants API with persistent memory via function calling | ⭐⭐ |

### JavaScript

| Example | Description | Complexity |
|---------|-------------|------------|
| [Next.js App](js/nextjs-app/) | Full-stack app with per-user AI memory | ⭐⭐ |
| [Vercel AI SDK](js/vercel-ai-sdk/) | Streaming chat with memory context injection | ⭐⭐ |
| [Discord Bot](js/discord-bot/) | Bot that remembers users across conversations | ⭐⭐ |

### Notebooks

| Example | Description |
|---------|-------------|
| [Getting Started](notebooks/getting-started.ipynb) | Interactive walkthrough — store, search, explore |

## Install

```bash
# Python SDK
pip install velixar

# JavaScript SDK
npm install velixar

# MCP Server (Claude, Cursor, VS Code)
npm install -g velixar-mcp-server
```

## Links

- [Documentation](https://docs.velixarai.com)
- [Python SDK](https://github.com/VelixarAi/velixar-python)
- [JavaScript SDK](https://github.com/VelixarAi/velixar-js)
- [MCP Server](https://github.com/VelixarAi/velixar-mcp-server)
- [CLI](https://github.com/VelixarAi/velixar-cli)
- [VS Code Extension](https://github.com/VelixarAi/velixar-vscode)

## License

MIT
