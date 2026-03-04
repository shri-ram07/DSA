from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        """
        Count the number of "special positions" in a binary matrix.

        A position (i, j) is considered special if:
        1. mat[i][j] == 1
        2. Row i contains exactly one '1'
        3. Column j contains exactly one '1'

        Approach:
        ----------
        - Iterate through each row of the matrix.
        - For each row, check if it contains exactly one '1'.
        - If yes, find the column index of that '1'.
        - Then check the entire column to ensure it also contains exactly one '1'.
        - If both conditions are satisfied, increment the count of special positions.

        Time Complexity:
        ----------------
        - Row check: O(n) per row (where n = number of columns).
        - Column check: O(m) per column (where m = number of rows).
        - Worst case: O(m * n), which is acceptable for typical constraints.

        Parameters:
        -----------
        mat : List[List[int]]
            A binary matrix (only 0s and 1s).

        Returns:
        --------
        int
            The number of special positions in the matrix.
        """

        count_ = 0  # Initialize counter for special positions

        # Iterate through each row by index
        for i in range(len(mat)):
            # Step 1: Check if row i has exactly one '1'
            if mat[i].count(1) == 1:
                # Step 2: Find the column index of that single '1'
                a = mat[i].index(1)

                # Step 3: Check if column 'a' has exactly one '1'
                # We build the sum by iterating through all rows
                if sum(mat[r][a] for r in range(len(mat))) == 1:
                    # Step 4: If both row and column checks pass, increment count
                    count_ += 1

        # Return the total number of special positions found
        return count_
