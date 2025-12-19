from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio
from transparent_ai.core.streaming import token_stream
from transparent_ai.examples.nodes import streaming_llm_node
from transparent_ai.core.state import ExecutionState
from transparent_ai.core.context import ExecutionContext
from transparent_ai.config.system import SystemConfig

app = FastAPI(title="Transparent AI Debugger")

LATEST_RUN = None


@app.post("/run")
def upload_run(run: dict):
    global LATEST_RUN
    LATEST_RUN = run
    return {"status": "ok"}


@app.get("/run")
def get_run():
    return LATEST_RUN

@app.get("/stream")
async def stream_tokens():
    async def event_generator():
        while True:
            token = await token_stream.get()
            yield f"data: {token}\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream"
    )

@app.get("/run-stream")
async def run_stream():
    async def event_generator():
        state = ExecutionState()
        context = ExecutionContext(
            run_id="live-stream",
            system_config=SystemConfig(system_prompt="stream")
        )

        # 🔥 INLINE streaming execution
        async for token in streaming_llm_node(state, context):
            yield f"data: {token}\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream"
    )
