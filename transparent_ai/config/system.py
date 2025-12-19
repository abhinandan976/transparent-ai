from pydantic import BaseModel


class SystemConfig(BaseModel):
    system_prompt: str
    temperature: float = 0.0
    max_tokens: int = 512
