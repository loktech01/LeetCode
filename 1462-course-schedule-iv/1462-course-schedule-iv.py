from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Initialize the isPrerequisite matrix
        isPrerequisite = [[False] * numCourses for _ in range(numCourses)]
        
        # Set direct prerequisites
        for a, b in prerequisites:
            isPrerequisite[a][b] = True
        
        # Apply Floyd-Warshall algorithm
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if isPrerequisite[i][k] and isPrerequisite[k][j]:
                        isPrerequisite[i][j] = True
        
        # Answer the queries
        return [isPrerequisite[u][v] for u, v in queries]
