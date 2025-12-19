from datetime import datetime
from transparent_ai.core.tracing import TraceEvent


class Executor:
    def __init__(self, graph):
        self.graph = graph

    async def run(self, start_node, state, context):
        queue = [start_node]

        while queue:
            node_name = queue.pop(0)
            node = self.graph.nodes[node_name]

            start_time = datetime.utcnow()
            state_before = state.model_dump()
            error = None

            try:
                state = await node.handler(state, context)
            except Exception as e:
                error = str(e)
                raise
            finally:
                end_time = datetime.utcnow()

                # 🔥 ALWAYS TRACE (even streaming nodes)
                state.traces.append(
                    TraceEvent(
                        node_name=node_name,
                        started_at=start_time,
                        ended_at=end_time,
                        duration_ms=(end_time - start_time).total_seconds() * 1000,
                        state_before=state_before,
                        state_after=state.model_dump(),
                        error=error,
                    )
                )

            if not state.should_continue:
                break

            for nxt in self.graph.edges.get(node_name, []):
                queue.append(nxt)

        return state
