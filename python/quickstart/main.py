# Velixar Quickstart — store and search memories in 10 lines
import os
from velixar import Velixar

v = Velixar(api_key=os.environ["VELIXAR_API_KEY"])

# Store memories
v.store("User prefers dark mode and Python", tags=["preferences"])
v.store("Working on a RAG pipeline with LangChain", tags=["project"])
v.store("Decided to use Qdrant over Pinecone for vector search", tags=["decision"])

# Search — Velixar finds relevant memories semantically
results = v.search("what programming language does the user like?")
for m in results:
    print(f"[{m.score:.2f}] {m.content}")

print()

results = v.search("what vector database are they using?")
for m in results:
    print(f"[{m.score:.2f}] {m.content}")
