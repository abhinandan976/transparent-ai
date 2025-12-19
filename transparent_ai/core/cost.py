from pydantic import BaseModel


class CostInfo(BaseModel):
    model_name: str
    tokens_used: int
    cost_usd: float
