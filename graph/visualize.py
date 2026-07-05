from graph.pipeline import graph

try:
    png = graph.get_graph().draw_mermaid_png()

    with open("graph.png", "wb") as f:
        f.write(png)

    print("✅ Graph saved as graph.png")

except Exception as e:
    print(f"Error: {e}")