def dfs(grid, i, j):
    """
    Depth-First Search (DFS) helper function to 'sink' an island.

    Parameters:
    -----------
    grid : List[List[str]]
        A 2D grid representing land ('1') and water ('0').
    i : int
        Current row index.
    j : int
        Current column index.

    Behavior:
    ---------
    - If the current cell is out of bounds or water ('0'), stop recursion.
    - Otherwise, mark the current land cell as visited by setting it to '0'.
    - Recursively explore all four directions (up, down, left, right).

    Visualization:
    --------------
    Imagine the grid as a map:

        1 1 0 0 0
        1 1 0 0 0
        0 0 1 0 0
        0 0 0 1 1

    When DFS finds a '1', it floods the entire connected island:

        Before DFS:
        [1,1,0,0,0]
        [1,1,0,0,0]
        [0,0,1,0,0]
        [0,0,0,1,1]

        After DFS starting at (0,0):
        [0,0,0,0,0]
        [0,0,0,0,0]
        [0,0,1,0,0]
        [0,0,0,1,1]

    This ensures the island is erased so it won’t be counted again.
    """
    # Base case: stop if out of bounds or water
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
        return

    # Mark current cell as visited (sink the land)
    grid[i][j] = "0"

    # Explore all four directions
    dfs(grid, i+1, j)  # Down
    dfs(grid, i-1, j)  # Up
    dfs(grid, i, j+1)  # Right
    dfs(grid, i, j-1)  # Left


class Solution(object):
    def numIslands(self, grid):
        """
        Count the number of islands in a 2D grid.

        Parameters:
        -----------
        grid : List[List[str]]
            A 2D grid of '1's (land) and '0's (water).

        Returns:
        --------
        int
            The number of distinct islands.

        Algorithm:
        ----------
        1. Iterate through every cell in the grid.
        2. When a '1' (land) is found:
            - Trigger DFS to erase the entire island.
            - Increment the island count.
        3. Continue scanning until all cells are processed.

        Time Complexity:
        ----------------
        O(n × m), where n = number of rows, m = number of columns.
        Each cell is visited at most once.

        Example Dry Run:
        ----------------
        Input grid:
            1 1 0 0 0
            1 1 0 0 0
            0 0 1 0 0
            0 0 0 1 1

        Step 1: Find (0,0) → DFS erases first island → count = 1
        Step 2: Find (2,2) → DFS erases second island → count = 2
        Step 3: Find (3,3) → DFS erases third island → count = 3

        Final Answer: 3 islands
        """
        if not grid or not grid[0]:
            return 0

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":  # Found new island
                    dfs(grid, i, j)    # Erase it
                    cnt += 1           # Increment island count
        return cnt
