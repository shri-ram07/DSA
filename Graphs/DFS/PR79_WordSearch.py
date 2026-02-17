class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Word Search (LeetCode Problem)

        Problem Summary:
        ----------------
        Given a 2D grid of characters and a target word, determine if the word
        can be constructed from letters of sequentially adjacent cells.
        Adjacent cells are horizontally or vertically neighboring.
        The same cell cannot be used more than once in a single word path.

        Approach:
        ---------
        - Use Depth‑First Search (DFS) starting from each cell that matches the
          first character of the word.
        - At each step:
            1. Check bounds and character match.
            2. If we’ve matched the last character, return True.
            3. Temporarily mark the current cell as visited (to avoid reuse).
            4. Explore all four neighbors (up, down, left, right).
            5. Restore the cell after exploring (backtracking).
        - If any DFS path returns True, the word exists.

        Diagram (Conceptual Example):
        -----------------------------
        Board:
            A B C E
            S F C S
            A D E E

        Word: "ABCCED"

        Path (visualized):
            A → B → C
                    ↓
                    C → E → D

        Each arrow shows DFS moving to a neighbor. Cells are marked visited
        during exploration and restored afterward.

        Time Complexity:
        ----------------
        O(M * N * 4^L)
        - M, N = board dimensions
        - L = length of word
        Worst case: try every cell as a start, and explore 4 directions per step.

        Space Complexity:
        -----------------
        O(L) recursion depth (stack frames).
        """

        m, n = len(board), len(board[0])

        def DFS(i, j, char_index):
            """
            Recursive DFS to check if word can be formed starting at (i, j).

            Parameters:
            -----------
            i, j : int
                Current cell coordinates.
            char_index : int
                Index of the character in 'word' we are trying to match.

            Returns:
            --------
            bool : True if path from (i, j) can complete the word, else False.
            """

            # 1. Out of bounds or mismatch
            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != word[char_index]:
                return False

            # 2. If we matched the last character, success
            if char_index == len(word) - 1:
                return True

            # 3. Mark current cell as visited
            temp = board[i][j]
            board[i][j] = "#"

            # 4. Explore neighbors
            neighbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
            for k, l in neighbors:
                if DFS(k, l, char_index + 1):
                    board[i][j] = temp  # restore before returning
                    return True

            # 5. Restore cell before backtracking
            board[i][j] = temp
            return False

        # Try starting DFS from every cell that matches first char
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and DFS(i, j, 0):
                    return True
        return False
