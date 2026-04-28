from app.utils.chart_generator import generate_bar_chart

def visualization_node(state):
    data = state.get("data", [])

    if not data or len(data) == 0:
        return {"chart_path": ""}

    # Auto-detect keys (basic logic)
    keys = list(data[0].keys())

    if len(keys) < 2:
        return {"chart_path": ""}

    x_key = keys[0]
    y_key = keys[1]

    chart_path = generate_bar_chart(data, x_key, y_key)

    return {
        "chart_path": chart_path
    }