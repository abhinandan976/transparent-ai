from pydantic import BaseModel
from transparent_ai.config.system import SystemConfig


class ExecutionContext(BaseModel):
    """
    Runtime context shared by all nodes.
    MCP-compatible.
    """
    run_id: str
    system_config: SystemConfig
    metadata: dict = {}
