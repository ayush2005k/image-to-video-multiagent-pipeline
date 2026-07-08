from langgraph.graph import StateGraph
from langgraph.graph import END

from state import PipelineState

from agents.intent_parser import intent_parser
from agents.image_analyzer import image_analyzer
from agents.image_selector import image_selector

from agents.storyboard_writer import storyboard_writer

builder = StateGraph(PipelineState)

# -------------------------
# Add Nodes
# -------------------------

builder.add_node(
    "intent_parser",
    intent_parser
)

builder.add_node(
    "image_analyzer",
    image_analyzer
)

builder.add_node(
    "image_selector",
    image_selector
)

builder.add_node(
    "storyboard_writer",
    storyboard_writer
)

# -------------------------
# Entry Point
# -------------------------

builder.set_entry_point(
    "intent_parser"
)

# -------------------------
# Edges
# -------------------------

builder.add_edge(
    "intent_parser",
    "image_analyzer"
)

builder.add_edge(
    "image_analyzer",
    "image_selector"
)

builder.add_edge(
    "image_selector",
    "storyboard_writer"
)
builder.add_edge(
    "storyboard_writer",
    END
)

# -------------------------
# Compile Graph
# -------------------------

graph = builder.compile()