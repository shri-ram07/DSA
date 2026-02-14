class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Edge case: if the matrix is empty, return an empty list immediately
        if not heights: 
            return []
        
        # Dimensions of the matrix
        m, n = len(heights), len(heights[0])

        # Sets to keep track of cells that can reach Pacific and Atlantic oceans
        pacific_reach = set()
        atlantic_reach = set()

        # Depth-First Search helper function
        def dfs(i, j, visited, prev_height):
            """
            Perform DFS from cell (i, j).
            - visited: set of cells already visited in this DFS run
            - prev_height: height of the previous cell to ensure water can flow
            """
            # Stop conditions:
            # 1. Already visited this cell
            # 2. Out of bounds
            # 3. Current cell height is lower than previous (water cannot flow uphill)
            if (i, j) in visited or i < 0 or j < 0 or i >= m or j >= n or heights[i][j] < prev_height:
                return
            
            # Mark this cell as visited (reachable from the ocean we started from)
            visited.add((i, j))

            # Explore all four directions (down, up, right, left)
            dfs(i+1, j, visited, heights[i][j])  # move down
            dfs(i-1, j, visited, heights[i][j])  # move up
            dfs(i, j+1, visited, heights[i][j])  # move right
            dfs(i, j-1, visited, heights[i][j])  # move left

        # Start DFS from Pacific Ocean edges:
        # Pacific touches the top row and the left column
        for i in range(m):
            dfs(i, 0, pacific_reach, heights[i][0])      # left edge
            dfs(i, n-1, atlantic_reach, heights[i][n-1]) # right edge (Atlantic)
        for j in range(n):
            dfs(0, j, pacific_reach, heights[0][j])      # top edge
            dfs(m-1, j, atlantic_reach, heights[m-1][j]) # bottom edge (Atlantic)

        # The result is the intersection of cells reachable from both oceans
        return list(pacific_reach & atlantic_reach)
