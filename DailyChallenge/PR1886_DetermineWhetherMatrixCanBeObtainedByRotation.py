from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        """
        Determine whether the target matrix can be obtained by rotating
        the given square matrix (mat) by 0°, 90°, 180°, or 270° clockwise.

        Approach:
        ----------
        1. Define a helper function `rotate` that rotates the matrix by 90° clockwise.
           - This is done by transposing the matrix and then reversing each row.
        2. Check the matrix against the target up to 4 times (0° + 3 rotations).
        3. If at any rotation the matrix equals the target, return True.
        4. If none match, return False.

        Why transpose + reverse?
        -------------------------
        - Transpose swaps rows and columns.
        - Reversing each row after transpose achieves a 90° clockwise rotation.
        - This avoids overwriting values mid‑iteration (the bug in your original code).

        Parameters:
        ------------
        mat : List[List[int]]
            The original n x n matrix.
        target : List[List[int]]
            The target n x n matrix we want to match.

        Returns:
        ---------
        bool
            True if target can be obtained by rotating mat, else False.
        """

        def rotate(matr: List[List[int]]) -> List[List[int]]:
            n = len(matr)
            # Step 1: Transpose the matrix (swap elements across the diagonal)
            for i in range(n):
                for j in range(i + 1, n):
                    matr[i][j], matr[j][i] = matr[j][i], matr[i][j]

            # Step 2: Reverse each row (to complete 90° clockwise rotation)
            for row in matr:
                row.reverse()

            return matr

        # Try all 4 possible rotations (0°, 90°, 180°, 270°)
        for _ in range(4):
            if mat == target:
                return True
            mat = rotate(mat)

        return False
