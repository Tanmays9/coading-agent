from langgraph.graph import END, START, StateGraph

from src.nodes.issue_reader import issue_reader_node
from src.nodes.planner import planner_node
from src.state import AgentState

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("issue_reader", issue_reader_node)
    graph.add_node("planner", planner_node)

    graph.add_edge(START, "issue_reader")
    graph.add_edge("issue_reader", "planner")
    graph.add_edge("planner", END)

    return graph.compile()