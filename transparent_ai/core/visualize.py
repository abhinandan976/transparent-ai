from transparent_ai.core.graph import Graph


def visualize_graph(graph: Graph):
    print("\nGRAPH STRUCTURE")

    for src, dsts in graph.edges.items():
        for dst in dsts:
            print(f"{src} ──▶ {dst}")


def visualize_trace_timeline(traces):
    print("\nEXECUTION TIMELINE")

    # 🔥 HARD GUARD (NO CRASH POSSIBLE)
    if traces is None or len(traces) == 0:
        print("(no trace events recorded)")
        return

    max_duration = max(t.duration_ms for t in traces)

    for idx, t in enumerate(traces, start=1):
        bar_len = int((t.duration_ms / max_duration) * 20)
        bar = "█" * max(bar_len, 1)

        print(
            f"[{idx}] {t.node_name:<8} |"
            f"{bar} {t.duration_ms:.2f}ms"
        )
