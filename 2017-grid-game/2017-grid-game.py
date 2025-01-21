from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        
        # Calculate prefix sums for the top and bottom rows
        prefix_top = [0] * n
        prefix_bottom = [0] * n
        
        prefix_top[0] = grid[0][0]
        prefix_bottom[0] = grid[1][0]
        
        for i in range(1, n):
            prefix_top[i] = prefix_top[i - 1] + grid[0][i]
            prefix_bottom[i] = prefix_bottom[i - 1] + grid[1][i]
        
        # Determine the minimum points the second robot can collect
        result = float('inf')
        
        for i in range(n):
            # Points left in the top row after column i
            top_remaining = prefix_top[n - 1] - prefix_top[i]
            # Points collected in the bottom row up to column i - 1
            bottom_collected = prefix_bottom[i - 1] if i > 0 else 0
            
            # Max points second robot can collect
            second_robot_points = max(top_remaining, bottom_collected)
            result = min(result, second_robot_points)
        
        return result
