from transparent_ai.schemas.messages import Message
from transparent_ai.schemas.llm_io import LLMResponse
from transparent_ai.core.context import ExecutionContext
import asyncio

class MockLLM:
    model_name = "mock-llm"

    async def generate(
        self,
        messages: list[Message],
        context: ExecutionContext
    ) -> LLMResponse:
        last = messages[-1].content.lower()

        if "calculate" in last:
            return LLMResponse(
                content="I should calculate step by step.",
                tokens_used=6
            )

        if "step" in last:
            return LLMResponse(
                content="Final answer: 2 + 3 = 5",
                tokens_used=6
            )

        return LLMResponse(
            content="I am thinking...",
            tokens_used=4
        )
    
    async def stream(self, messages, context):
        response = "Final answer: 2 + 3 = 5"
        for token in response.split():
            await asyncio.sleep(0.2)  # simulate latency
            yield token
