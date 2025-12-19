from pydantic import BaseModel


class AddInput(BaseModel):
    a: int
    b: int


class AddOutput(BaseModel):
    result: int


async def add(input: AddInput) -> AddOutput:
    return AddOutput(result=input.a + input.b)


add.name = "add"
add.input_schema = AddInput
add.output_schema = AddOutput
