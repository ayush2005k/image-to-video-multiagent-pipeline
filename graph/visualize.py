from graph.pipeline import graph

graph.get_graph().draw_mermaid_png(

    output_file_path="graph.png"

)

print("Graph Saved!")