from pydantic import BaseModel
from typing import Any, Dict, List
from transparent_ai.schemas.messages import Message
from transparent_ai.core.tracing import TraceEvent
from transparent_ai.core.cost import CostInfo


class ExecutionState(BaseModel):
    # Conversation
    messages: List[Message] = []

    # Explicit memory + outputs
    memory: Dict[str, Any] = {}
    outputs: Dict[str, Any] = {}

    # Agent loop control
    step_count: int = 0
    max_steps: int = 5
    should_continue: bool = True

    # Tracing
    traces: List[TraceEvent] = []

    # 🔥 COST & TOKEN ACCOUNTING (FIX)
    costs: List[CostInfo] = []
    total_tokens: int = 0
    total_cost_usd: float = 0.0
