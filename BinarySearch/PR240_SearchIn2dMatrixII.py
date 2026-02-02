class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        Search a target value in a 2D matrix using the "staircase search" algorithm.

        The matrix has the following properties:
        - Integers in each row are sorted in ascending order (left to right).
        - Integers in each column are sorted in ascending order (top to bottom).

        Approach:
        ----------
        We start from the **top-right corner** of the matrix:
        - If the current element == target → return True.
        - If the current element < target → move **down** (increase row index).
        - If the current element > target → move **left** (decrease column index).
        - Continue until we either find the target or go out of bounds.

        Time Complexity: O(m + n), where m = number of rows, n = number of columns.
        Space Complexity: O(1), since we only use pointers.

        Example Matrix:
        ----------------
        [
          [ 1,  4,  7, 11, 15],
          [ 2,  5,  8, 12, 19],
          [ 3,  6,  9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]
        ]

        Diagram of Search Path:
        ------------------------
        Start at top-right (15):
        
        (row=0, col=4) → 15 > 18 → move left
        (row=0, col=3) → 11 < 18 → move down
        (row=1, col=3) → 12 < 18 → move down
        (row=2, col=3) → 16 < 18 → move down
        (row=3, col=3) → 17 < 18 → move down
        (row=4, col=3) → 26 > 18 → move left
        (row=4, col=2) → 23 > 18 → move left
        (row=4, col=1) → 21 > 18 → move left
        (row=4, col=0) → 18 == target → FOUND ✅

        Returns:
        --------
        True if target exists in matrix, False otherwise.
        """

        # Start from top-right corner
        row, col = 0, len(matrix[0]) - 1  

        # Loop until we go out of bounds
        while row < len(matrix) and col >= 0:
            # Debug print to trace the search path
            print("Checking position:", row, col, "→ value:", matrix[row][col])

            if matrix[row][col] == target:
                return True  # Target found
            elif matrix[row][col] < target:
                row += 1  # Move down
            else:
                col -= 1  # Move left

        return False  # Target not found


# Example usage
o = Solution()
a = o.searchMatrix(
    [[1,4,7,11,15],
     [2,5,8,12,19],
     [3,6,9,16,22],
     [10,13,14,17,24],
     [18,21,23,26,30]], 
    18
)
print("Result:", a)
