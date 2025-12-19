from typing import Protocol
from transparent_ai.schemas.messages import Message
from transparent_ai.schemas.llm_io import LLMResponse
from transparent_ai.core.context import ExecutionContext
from typing import AsyncIterator

class LLM(Protocol):
    model_name: str

    async def generate(
        self,
        messages: list[Message],
        context: ExecutionContext
    ) -> LLMResponse:
        ...

    async def stream(
        self,
        messages,
        context
    ) -> AsyncIterator[str]:
        ...
