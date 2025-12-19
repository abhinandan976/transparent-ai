from transparent_ai.core.state import ExecutionState


def export_run(state: ExecutionState) -> dict:
    # JSON-safe export (datetimes → ISO strings)
    return state.model_dump(mode="json")

