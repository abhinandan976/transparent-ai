from transparent_ai.core.state import ExecutionState
from transparent_ai.core.context import ExecutionContext
from transparent_ai.schemas.messages import Message
from transparent_ai.adapters.mock_llm import MockLLM
from transparent_ai.config.pricing import MODEL_PRICING
from transparent_ai.core.cost import CostInfo
from transparent_ai.core.streaming import token_stream
from transparent_ai.schemas.messages import Message

# -------------------------------------------------
# USER INPUT NODE
# -------------------------------------------------
async def user_input_node(
    state: ExecutionState,
    context: ExecutionContext
):
    state.messages.append(
        Message(role="user", content="What is 2 + 3?")
    )
    return state


# -------------------------------------------------
# AGENT REASONING NODE
# -------------------------------------------------
llm = MockLLM()

async def agent_reasoning_node(
    state: ExecutionState,
    context: ExecutionContext
):
    response = await llm.generate(state.messages, context)

    price_per_token = MODEL_PRICING.get(llm.model_name, 0.0)
    cost = response.tokens_used * price_per_token

    state.total_tokens += response.tokens_used
    state.total_cost_usd += cost

    state.costs.append(
        CostInfo(
            model_name=llm.model_name,
            tokens_used=response.tokens_used,
            cost_usd=cost,
       )
    )


    state.messages.append(
        Message(role="assistant", content=response.content)
    )

    state.step_count += 1
    return state


# -------------------------------------------------
# DECISION NODE (STOP / CONTINUE)
# -------------------------------------------------
async def decision_node(
    state: ExecutionState,
    context: ExecutionContext
):
    last = state.messages[-1].content.lower()

    if "final answer" in last:
        state.should_continue = False

    if state.step_count >= state.max_steps:
        state.should_continue = False

    return state


# -------------------------------------------------
# ROUTER NODE (NO-OP)
# -------------------------------------------------
async def loop_router_node(
    state: ExecutionState,
    context: ExecutionContext
):
    return state

async def streaming_llm_node(state, context):
    print("✅ STREAMING NODE STARTED")

    collected = []

    async for token in llm.stream(state.messages, context):
        print("➡ TOKEN:", token)      # PROOF
        await token_stream.put(token) # SEND TO SSE
        collected.append(token)

    final_text = " ".join(collected)

    state.messages.append(
        Message(role="assistant", content=final_text)
    )

    state.should_continue = False
    return state