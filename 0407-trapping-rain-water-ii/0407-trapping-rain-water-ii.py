import heapq

class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []
        
        # Push all boundary cells into the min-heap
        for i in range(m):
            for j in [0, n - 1]:  # First and last column
                heapq.heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True
        for j in range(1, n - 1):
            for i in [0, m - 1]:  # First and last row
                heapq.heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True
        
        # Directions for moving to neighbors
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        water_trapped = 0
        
        while heap:
            height, x, y = heapq.heappop(heap)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    # Calculate trapped water
                    water_trapped += max(0, height - heightMap[nx][ny])
                    # Update boundary with the new height
                    heapq.heappush(heap, (max(height, heightMap[nx][ny]), nx, ny))
        
        return water_trapped
