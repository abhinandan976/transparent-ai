from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict, Any


class TraceEvent(BaseModel):
    node_name: str
    started_at: datetime
    ended_at: datetime
    duration_ms: float
    state_before: Dict[str, Any]
    state_after: Dict[str, Any]
    error: Optional[str] = None
