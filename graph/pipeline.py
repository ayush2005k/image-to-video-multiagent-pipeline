from langgraph.graph import StateGraph
from langgraph.graph import END

from state import PipelineState

from agents.intent_parser import intent_parser
from agents.image_analyzer import image_analyzer

builder = StateGraph(PipelineState)

builder.add_node(
    "intent_parser",
    intent_parser
)

builder.add_node(
    "image_analyzer",
    image_analyzer
)

builder.set_entry_point(
    "intent_parser"
)

builder.add_edge(
    "intent_parser",
    "image_analyzer"
)

builder.add_edge(
    "image_analyzer",
    END
)

graph = builder.compile()