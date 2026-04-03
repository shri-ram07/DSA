from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        Find the shortest path in a binary matrix using BFS.

        Problem:
        - You are given an n x n binary matrix 'grid'.
        - Each cell is either 0 (open) or 1 (blocked).
        - You can move in 8 directions (horizontal, vertical, diagonal).
        - The goal is to find the shortest path from the top-left (0,0)
          to the bottom-right (n-1,n-1).
        - Return the length of the shortest path, or -1 if no path exists.

        Approach:
        - Use Breadth-First Search (BFS) because it guarantees shortest path
          in an unweighted grid.
        - Start from (0,0) if it is open.
        - Explore neighbors in all 8 directions.
        - Track visited cells to avoid revisiting.
        - Stop when reaching (n-1,n-1).

        Complexity:
        - Time: O(n^2) because each cell is visited at most once.
        - Space: O(n^2) for the queue and visited set.
        """

        n = len(grid)

        # Early exit: if start or end is blocked, no path exists
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1

        # Directions: 8 possible moves (up, down, left, right, diagonals)
        directions = [(1,0), (-1,0), (0,1), (0,-1),
                      (1,1), (-1,-1), (1,-1), (-1,1)]

        # BFS queue: stores ((row, col), path_length)
        queue = deque([((0, 0), 1)])

        # Visited set: ensures each cell is processed only once
        visited = {(0, 0)}

        # BFS loop
        while queue:
            (i, j), level = queue.popleft()

            # If we reached the bottom-right cell, return path length
            if i == n-1 and j == n-1:
                return level

            # Explore all 8 neighbors
            for dx, dy in directions:
                k, l = i + dx, j + dy

                # Check bounds, open cell, and not visited
                if 0 <= k < n and 0 <= l < n and grid[k][l] == 0 and (k, l) not in visited:
                    queue.append(((k, l), level+1))
                    visited.add((k, l))

        # If BFS finishes without reaching target, no path exists
        return -1
