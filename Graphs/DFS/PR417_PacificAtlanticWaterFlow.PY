# class Solution:
#     def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
#         # Edge case: if the matrix is empty, return an empty list immediately
#         if not heights: 
#             return []
        
#         # Dimensions of the matrix
#         m, n = len(heights), len(heights[0])

#         # Sets to keep track of cells that can reach Pacific and Atlantic oceans
#         pacific_reach = set()
#         atlantic_reach = set()

#         # Depth-First Search helper function
#         def dfs(i, j, visited, prev_height):
#             """
#             Perform DFS from cell (i, j).
#             - visited: set of cells already visited in this DFS run
#             - prev_height: height of the previous cell to ensure water can flow
#             """
#             # Stop conditions:
#             # 1. Already visited this cell
#             # 2. Out of bounds
#             # 3. Current cell height is lower than previous (water cannot flow uphill)
#             if (i, j) in visited or i < 0 or j < 0 or i >= m or j >= n or heights[i][j] < prev_height:
#                 return
            
#             # Mark this cell as visited (reachable from the ocean we started from)
#             visited.add((i, j))

#             # Explore all four directions (down, up, right, left)
#             dfs(i+1, j, visited, heights[i][j])  # move down
#             dfs(i-1, j, visited, heights[i][j])  # move up
#             dfs(i, j+1, visited, heights[i][j])  # move right
#             dfs(i, j-1, visited, heights[i][j])  # move left

#         # Start DFS from Pacific Ocean edges:
#         # Pacific touches the top row and the left column
#         for i in range(m):
#             dfs(i, 0, pacific_reach, heights[i][0])      # left edge
#             dfs(i, n-1, atlantic_reach, heights[i][n-1]) # right edge (Atlantic)
#         for j in range(n):
#             dfs(0, j, pacific_reach, heights[0][j])      # top edge
#             dfs(m-1, j, atlantic_reach, heights[m-1][j]) # bottom edge (Atlantic)

#         # The result is the intersection of cells reachable from both oceans
#         return list(pacific_reach & atlantic_reach)




class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Pacific Atlantic Water Flow Problem (LeetCode 417)

        Given an m x n matrix of heights, determine which cells can flow water
        to both the Pacific and Atlantic oceans. Water can only flow from a cell
        to its neighboring cell (up, down, left, right) if the neighbor's height
        is less than or equal to the current cell's height.

        Approach:
        ----------
        1. Pacific touches the **top row** and **left column**.
        2. Atlantic touches the **bottom row** and **right column**.
        3. Instead of starting DFS from each cell, we start DFS from the oceans
           inward:
            - Run DFS from all Pacific edge cells → mark reachable cells.
            - Run DFS from all Atlantic edge cells → mark reachable cells.
        4. The intersection of these two sets/matrices gives the cells that can
           reach both oceans.

        Time Complexity: O(m * n) because each cell is visited at most twice.
        Space Complexity: O(m * n) for the visited matrices.

        Diagram (example 3x3 grid):
        
              Pacific Edge ↑
              ┌───┬───┬───┐
        ←     │(0,0) (0,1) (0,2)│     →
        Left   │(1,0) (1,1) (1,2)│   Right
        Edge   │(2,0) (2,1) (2,2)│   Edge
              └───┴───┴───┘
              ↓ Atlantic Edge

        - Pacific DFS starts from top row and left column.
        - Atlantic DFS starts from bottom row and right column.
        - Cells reachable by both DFS runs are the answer.
        """

        if not heights: 
            return []
        m, n = len(heights), len(heights[0])

        def dfs(i, j, eligible, pr):
            """
            DFS helper function:
            - i, j: current cell coordinates
            - eligible: matrix marking visited cells for Pacific or Atlantic
            - pr: previous cell's height (to ensure valid water flow)
            """
            # Stop if out of bounds, height is lower than previous, or already visited
            if i < 0 or j < 0 or i >= m or j >= n or heights[i][j] < pr or eligible[i][j]:
                return

            # Mark current cell as reachable
            eligible[i][j] = True

            # Explore all four directions
            dfs(i+1, j, eligible, heights[i][j])  # Down
            dfs(i-1, j, eligible, heights[i][j])  # Up
            dfs(i, j+1, eligible, heights[i][j])  # Right
            dfs(i, j-1, eligible, heights[i][j])  # Left

        # Matrices to mark reachability from Pacific and Atlantic
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]

        # DFS from Pacific edges (top row and left column)
        for i in range(m):
            dfs(i, 0, pacific, heights[i][0])        # Left edge
            dfs(i, n-1, atlantic, heights[i][n-1])   # Right edge
        for j in range(n):
            dfs(0, j, pacific, heights[0][j])        # Top edge
            dfs(m-1, j, atlantic, heights[m-1][j])   # Bottom edge

        # Collect cells that can reach both oceans
        result = []
        for x in range(m):
            for y in range(n):
                if pacific[x][y] and atlantic[x][y]:
                    result.append([x, y])

        return result
