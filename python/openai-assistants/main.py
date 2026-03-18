# OpenAI Assistants + Velixar — persistent memory via function calling
import os, json
from velixar import Velixar
from openai import OpenAI

v = Velixar(api_key=os.environ["VELIXAR_API_KEY"])
oai = OpenAI()

tools = [
    {"type": "function", "function": {
        "name": "remember",
        "description": "Store something important about the user for future recall",
        "parameters": {"type": "object", "properties": {
            "content": {"type": "string", "description": "What to remember"},
            "tags": {"type": "array", "items": {"type": "string"}, "description": "Tags"}
        }, "required": ["content"]}}},
    {"type": "function", "function": {
        "name": "recall",
        "description": "Search memory for relevant context about the user",
        "parameters": {"type": "object", "properties": {
            "query": {"type": "string", "description": "What to search for"}
        }, "required": ["query"]}}},
]


def handle_tool_call(call):
    args = json.loads(call.function.arguments)
    if call.function.name == "remember":
        result = v.store(args["content"], tags=args.get("tags", []))
        return f"Stored memory: {result.id}"
    elif call.function.name == "recall":
        results = v.search(args["query"], limit=3)
        return "\n".join(f"- {m.content}" for m in results) or "No memories found."


def chat(message: str):
    messages = [
        {"role": "system", "content": "You have access to persistent memory. Use 'remember' to store important facts and 'recall' to search for context. Always check memory before answering personal questions."},
        {"role": "user", "content": message},
    ]
    resp = oai.chat.completions.create(model="gpt-4o-mini", messages=messages, tools=tools)

    while resp.choices[0].message.tool_calls:
        messages.append(resp.choices[0].message)
        for call in resp.choices[0].message.tool_calls:
            result = handle_tool_call(call)
            messages.append({"role": "tool", "tool_call_id": call.id, "content": result})
        resp = oai.chat.completions.create(model="gpt-4o-mini", messages=messages, tools=tools)

    print(f"AI: {resp.choices[0].message.content}")


if __name__ == "__main__":
    chat("My name is Luke and I'm building Velixar, a cognitive memory platform.")
    chat("I prefer Python and serverless architecture on AWS.")
    chat("What do you know about me?")
