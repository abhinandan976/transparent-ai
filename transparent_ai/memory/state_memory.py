from transparent_ai.core.state import ExecutionState


class StateMemory:
    async def read(self, state: ExecutionState) -> ExecutionState:
        return state

    async def write(self, state: ExecutionState) -> ExecutionState:
        return state
