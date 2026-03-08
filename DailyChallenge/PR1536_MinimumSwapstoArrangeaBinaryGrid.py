class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        """
        LeetCode 1536: Minimum Swaps to Arrange a Binary Grid

        Problem:
        Given an n x n binary grid, we want to rearrange rows (by swapping entire rows)
        so that for every row i, the number of trailing zeros in that row is at least
        (n - i - 1). If it's impossible, return -1.

        Approach:
        1. Count trailing zeros for each row.
        2. For each row i, check if it meets the requirement (n - i - 1).
        3. If not, search downward for the first row that satisfies the requirement.
        4. Swap that row upward, counting the number of swaps.
        5. If no row can satisfy the requirement, return -1.
        6. Return the total number of swaps performed.

        Time Complexity: O(n^2) (worst case scanning rows)
        Space Complexity: O(n) (storing trailing zeros)
        """

        n = len(grid)

        # Step 1: Count trailing zeros for each row
        trailing_zeros = []
        for row in grid:
            count = 0
            # Traverse row from right to left
            for val in reversed(row):
                if val == 0:
                    count += 1
                else:
                    # Stop counting once we hit a '1'
                    break
            trailing_zeros.append(count)

        swaps = 0

        # Step 2: Check each row requirement
        for i in range(n):
            required = n - i - 1  # Minimum trailing zeros needed for row i

            # If current row doesn't meet requirement
            if trailing_zeros[i] < required:
                j = i + 1
                # Step 3: Look downward for a row that satisfies requirement
                while j < n and trailing_zeros[j] < required:
                    j += 1

                # If no row found, arrangement is impossible
                if j == n:
                    return -1

                # Step 4: Swap row j upward to position i
                while j > i:
                    # Bubble row j up one step at a time
                    trailing_zeros[j], trailing_zeros[j-1] = trailing_zeros[j-1], trailing_zeros[j]
                    swaps += 1
                    j -= 1

        # Step 5: Return total swaps performed
        return swaps
