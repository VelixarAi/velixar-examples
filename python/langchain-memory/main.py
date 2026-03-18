# LangChain + Velixar — persistent memory for any chain
import os
from velixar import Velixar
from langchain_core.memory import BaseMemory
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from pydantic import PrivateAttr


class VelixarMemory(BaseMemory):
    """LangChain memory backend powered by Velixar."""
    _client: Velixar = PrivateAttr()
    _user_id: str = PrivateAttr()

    def __init__(self, user_id: str = "default", **kwargs):
        super().__init__(**kwargs)
        self._client = Velixar(api_key=os.environ["VELIXAR_API_KEY"])
        self._user_id = user_id

    @property
    def memory_variables(self) -> list[str]:
        return ["history"]

    def load_memory_variables(self, inputs: dict) -> dict:
        query = inputs.get("input", "")
        results = self._client.search(query, limit=3)
        history = "\n".join(f"- {m.content}" for m in results)
        return {"history": history or "No prior context."}

    def save_context(self, inputs: dict, outputs: dict) -> None:
        exchange = f"Human: {inputs['input']}\nAI: {outputs['response']}"
        self._client.store(exchange, tags=["conversation", f"user:{self._user_id}"])

    def clear(self) -> None:
        pass


if __name__ == "__main__":
    memory = VelixarMemory(user_id="demo_user")
    llm = ChatOpenAI(model="gpt-4o-mini")
    chain = ConversationChain(llm=llm, memory=memory, verbose=True)

    # The AI remembers across sessions — restart this script and it still knows
    chain.predict(input="My name is Luke and I'm building a cognitive memory platform.")
    chain.predict(input="I prefer Python over JavaScript for backend work.")
    chain.predict(input="What do you remember about me?")
