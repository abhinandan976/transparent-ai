from typing import Callable, Dict, List


class Node:
    def __init__(self, name: str, handler: Callable):
        self.name = name
        self.handler = handler


class Graph:
    def __init__(self):
        self.nodes: Dict[str, Node] = {}
        self.edges: Dict[str, List[str]] = {}

    def add_node(self, node: Node):
        self.nodes[node.name] = node

    def add_edge(self, src: str, dst: str):
        self.edges.setdefault(src, []).append(dst)
