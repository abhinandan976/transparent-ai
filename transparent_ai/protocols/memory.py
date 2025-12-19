from typing import Protocol
from transparent_ai.core.state import ExecutionState


class Memory(Protocol):
    async def read(self, state: ExecutionState) -> ExecutionState:
        ...

    async def write(self, state: ExecutionState) -> ExecutionState:
        ...
