from collections import deque
from typing import List

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        # Dimensions of the matrix
        m, n = len(isWater), len(isWater[0])
        
        # Initialize the height matrix with -1 (unvisited)
        height = [[-1 for _ in range(n)] for _ in range(m)]
        
        # Initialize the BFS queue
        queue = deque()
        
        # Add all water cells to the queue and set their height to 0
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    queue.append((i, j))
                    height[i][j] = 0
        
        # Directions for moving to adjacent cells (north, south, east, west)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Perform BFS
        while queue:
            x, y = queue.popleft()
            
            # Process all adjacent cells
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # Check if the neighbor is within bounds and unvisited
                if 0 <= nx < m and 0 <= ny < n and height[nx][ny] == -1:
                    # Set the height of the neighbor
                    height[nx][ny] = height[x][y] + 1
                    # Add the neighbor to the queue
                    queue.append((nx, ny))
        
        return height
