from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])  # Path compression
            return parent[x]

        def union(parent, rank, x, y):
            root_x = find(parent, x)
            root_y = find(parent, y)
            if root_x == root_y:
                return False  # Cycle detected
            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            elif rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            else:
                parent[root_y] = root_x
                rank[root_x] += 1
            return True

        n = len(edges)
        parent = list(range(n + 1))
        rank = [0] * (n + 1)

        for u, v in edges:
            if not union(parent, rank, u, v):
                return [u, v]  # The redundant edge forming a cycle
