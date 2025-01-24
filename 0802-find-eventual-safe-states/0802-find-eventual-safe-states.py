from collections import deque, defaultdict
from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)  # Number of nodes in the graph
        
        # Step 1: Reverse the graph and compute out-degrees
        reverse_graph = defaultdict(list)
        out_degree = [0] * n  # Out-degree of each node in the original graph
        
        for node in range(n):
            for neighbor in graph[node]:
                reverse_graph[neighbor].append(node)
            out_degree[node] = len(graph[node])
        
        # Step 2: Initialize a queue with terminal nodes (out-degree = 0)
        queue = deque([node for node in range(n) if out_degree[node] == 0])
        
        # Step 3: Perform reverse topological sort
        safe_nodes = []
        
        while queue:
            curr = queue.popleft()
            safe_nodes.append(curr)
            
            for neighbor in reverse_graph[curr]:
                out_degree[neighbor] -= 1
                if out_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 4: Return sorted list of safe nodes
        return sorted(safe_nodes)
