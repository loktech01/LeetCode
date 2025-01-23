from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # Dimensions of the grid
        m, n = len(grid), len(grid[0])
        
        # Arrays to store the count of servers in each row and column
        row_count = [0] * m
        col_count = [0] * n
        
        # Count the servers in each row and column
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1
        
        # Count the servers that can communicate
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (row_count[i] > 1 or col_count[j] > 1):
                    count += 1
        
        return count
