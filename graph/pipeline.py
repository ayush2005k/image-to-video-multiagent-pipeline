from langgraph.graph import StateGraph

from langgraph.graph import END

from state import PipelineState

from agents.intent_parser import intent_parser

builder = StateGraph(PipelineState)

builder.add_node(

    "intent_parser",

    intent_parser

)

builder.set_entry_point(

    "intent_parser"

)

builder.add_edge(

    "intent_parser",

    END

)

graph = builder.compile()