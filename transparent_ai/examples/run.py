import asyncio
from transparent_ai.core.graph import Graph, Node
from transparent_ai.core.executor import Executor
from transparent_ai.core.state import ExecutionState
from transparent_ai.core.context import ExecutionContext
from transparent_ai.config.system import SystemConfig
from transparent_ai.examples.nodes import user_input_node, streaming_llm_node


async def main():
    graph = Graph()

    graph.add_node(Node("input", user_input_node))
    graph.add_node(Node("stream", streaming_llm_node))

    graph.add_edge("input", "stream")

    executor = Executor(graph)

    state = ExecutionState()

    context = ExecutionContext(
        run_id="stream-demo",
        system_config=SystemConfig(system_prompt="stream")
    )

    await executor.run("input", state, context)


asyncio.run(main())
