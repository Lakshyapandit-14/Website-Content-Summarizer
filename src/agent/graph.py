from typing import Any, Callable, Dict, List

class Node:
    def __init__(self, name: str, run_fn: Callable[..., Any]):
        self.name = name
        self.run_fn = run_fn

    async def run(self, **kwargs):
        return await self.run_fn(**kwargs) if callable(self.run_fn) and getattr(self.run_fn, "__code__", None) else self.run_fn(**kwargs)

class Graph:
    def __init__(self):
        self.nodes: List[Node] = []

    def add_node(self, node: Node):
        self.nodes.append(node)

    async def run(self, initial: Dict = None):
        state = initial or {}
        for node in self.nodes:
            res = await node.run(**state) if hasattr(node.run, "__call__") else node.run(**state)
            if isinstance(res, dict):
                state.update(res)
            else:
                state[node.name] = res
        return state
