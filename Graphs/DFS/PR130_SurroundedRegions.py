class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Surrounded Regions (LeetCode 130)

        Problem:
        - Given a 2D board containing 'X' and 'O'.
        - Capture all regions surrounded by 'X' by flipping surrounded 'O' → 'X'.
        - Boundary-connected 'O's should remain unchanged.

        Approach (DFS):
        1. Traverse the boundary of the board.
        2. For each boundary 'O', run DFS to mark all connected 'O's as safe ('T').
        3. After DFS:
           - Flip all remaining 'O' → 'X' (captured).
           - Flip all 'T' → 'O' (restore safe ones).

        Why this works:
        - Any 'O' connected to the boundary cannot be captured.
        - By marking them first, we isolate the truly surrounded regions.

        Diagram Example:
        Input:
            X X X X
            X O O X
            X X O X
            X O X X

        Step 1: Mark boundary-connected 'O's → 'T'
            X X X X
            X O O X
            X X O X
            X T X X

        Step 2: DFS spreads 'T' to connected 'O's
            X X X X
            X O O X
            X X O X
            X T X X

        Step 3: Flip remaining 'O' → 'X', 'T' → 'O'
        Output:
            X X X X
            X X X X
            X X X X
            X O X X

        Complexity:
        - Time: O(m * n), each cell visited at most once.
        - Space: O(m * n) recursion stack in worst case.
        """

        def DFS(i, j):
            # Base case: out of bounds or not 'O'
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
                return

            # Mark as safe
            board[i][j] = 'T'

            # Explore neighbors (up, down, left, right)
            DFS(i - 1, j)
            DFS(i + 1, j)
            DFS(i, j - 1)
            DFS(i, j + 1)

        m, n = len(board), len(board[0])

        # Step 1: Run DFS from boundary 'O's
        for i in range(m):
            DFS(i, 0)       # left boundary
            DFS(i, n - 1)   # right boundary
        for j in range(n):
            DFS(0, j)       # top boundary
            DFS(m - 1, j)   # bottom boundary

        # Step 2: Flip cells
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'  # captured
                elif board[i][j] == 'T':
                    board[i][j] = 'O'  # restore safe
