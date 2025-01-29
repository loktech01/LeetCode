from typing import List

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            # Base case: If out of bounds, land cell, or already visited
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0 or visited[r][c]:
                return 0
            
            # Mark as visited
            visited[r][c] = True
            
            # Collect fish from the current cell
            fish_count = grid[r][c]
            
            # Explore all adjacent cells
            for dr, dc in directions:
                fish_count += dfs(r + dr, c + dc)
            
            return fish_count

        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        max_fish = 0
        
        # Iterate over all cells in the grid
        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0 and not visited[r][c]:
                    # Start DFS from this cell
                    max_fish = max(max_fish, dfs(r, c))
        
        return max_fish
