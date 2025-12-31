from langgraph.graph import END, StateGraph
from typing_extensions import TypedDict

# Define the state object
class GraphState(TypedDict):
    question: str
    context: str
    generation: str

# Initialize the Graph
workflow = StateGraph(GraphState)

# Define Nodes (Imported from nodes.py)
workflow.add_node("router", question_router)
workflow.add_node("web_search", web_search_node)
workflow.add_node("generate", categorization_node)

# Define Edges with Conditional Logic
workflow.set_entry_point("router")
workflow.add_conditional_edges(
    "router",
    lambda x: x["datasource"],
    {
        "web_search": "web_search",
        "generate": "generate",
    },
)
workflow.add_edge("web_search", "generate")
workflow.add_edge("generate", END)

app = workflow.compile()
