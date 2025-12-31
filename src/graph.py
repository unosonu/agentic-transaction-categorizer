from langgraph.graph import END, StateGraph
from .nodes import web_search_node, categorization_node

workflow = StateGraph(GraphState)

# Define the conditional routing logic
def route_question(state):
    # This logic comes from your 'router_chain'
    # If the LLM returns 'web_search', we go to the scraper
    if state["datasource"] == "web_search":
        return "web_search"
    return "generate"

workflow.add_node("web_search", web_search_node)
workflow.add_node("generate", categorization_node)

workflow.set_entry_point("router") # Router is a node that sets 'datasource'
workflow.add_conditional_edges(
    "router",
    route_question,
    {
        "web_search": "web_search",
        "generate": "generate",
    },
)
workflow.add_edge("web_search", "generate")
workflow.add_edge("generate", END)
