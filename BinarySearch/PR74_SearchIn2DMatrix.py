class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        Search a target value in a 2D matrix using binary search.

        The matrix has the following properties:
        - Each row is sorted in ascending order.
        - The first integer of each row is greater than the last integer of the previous row.

        Diagram (example matrix):
            [
              [ 1,  3,  5],
              [ 7,  9, 11],
              [13, 15, 17]
            ]

        Target search idea:
        1. First, binary search on rows:
            - Compare target with first and last element of mid row.
            - If target < first element → move search to upper rows.
            - If target > last element → move search to lower rows.
            - Else → target must be inside this row.
        2. Then, binary search inside that row.
        """

        # Step 1: Binary search to find the correct row
        i, j = 0, len(matrix) - 1
        while i <= j:
            mid = (i + j) // 2
            if matrix[mid][0] > target:
                j = mid - 1   # target is smaller → search upper half
            elif matrix[mid][-1] < target:
                i = mid + 1   # target is larger → search lower half
            else:
                break         # target lies within this row
        else:
            return False      # no row contains the target

        # Step 2: Binary search inside the chosen row
        arr = matrix[mid]
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] == target:
                return True   # found target
            elif target < arr[mid]:
                r = mid - 1   # target is smaller → move left
            else:
                l = mid + 1   # target is larger → move right

        return False          # target not found
