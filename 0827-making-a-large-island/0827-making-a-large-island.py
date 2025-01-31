from collections import defaultdict
from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island_sizes = {0: 0}  # Map island index to size, 0 is reserved for water
        island_id = 2  # Start marking islands from 2
        directions = [(0,1), (0,-1), (1,0), (-1,0)]  # 4-directional movement

        # Step 1: Find all islands and assign unique IDs
        def dfs(r, c, index):
            if r < 0 or c < 0 or r >= n or c >= n or grid[r][c] != 1:
                return 0
            grid[r][c] = index  # Mark the cell with the island ID
            size = 1
            for dr, dc in directions:
                size += dfs(r + dr, c + dc, index)
            return size

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:  # Found a new island
                    island_sizes[island_id] = dfs(r, c, island_id)
                    island_id += 1  # Move to next unique ID

        # Step 2: Find the max island size by flipping one 0
        max_island = max(island_sizes.values(), default=0)  # In case no islands exist
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:  # Try flipping this 0
                    seen_islands = set()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            seen_islands.add(grid[nr][nc])  # Collect unique island IDs
                    
                    # Compute new possible island size
                    new_island_size = 1 + sum(island_sizes[i] for i in seen_islands)
                    max_island = max(max_island, new_island_size)

        return max_island
