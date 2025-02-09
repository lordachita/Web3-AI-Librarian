from backend.graphs import Graph
from backend.utils import load_env

load_env()
graph = Graph(is_memory = True)
graph = graph.compile()
