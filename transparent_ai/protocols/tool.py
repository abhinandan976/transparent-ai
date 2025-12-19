from typing import Protocol, runtime_checkable
from pydantic import BaseModel


@runtime_checkable
class Tool(Protocol):
    name: str
    input_schema: type[BaseModel]
    output_schema: type[BaseModel]

    async def __call__(self, input: BaseModel) -> BaseModel:
        ...
