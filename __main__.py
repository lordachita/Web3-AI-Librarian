from backend.graphs import Graph
from backend.utils import load_env

load_env()

graph = Graph(is_memory = True)
prompt = (
    "What is the key difference between Sahara, Story and Sentient projects?"
)

s = graph.stream(prompt)