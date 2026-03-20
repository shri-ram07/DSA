class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        """
        Compute the minimum absolute difference between distinct elements
        in every k x k submatrix of the given grid.

        Args:
            grid (List[List[int]]): 2D matrix of integers.
            k (int): Size of the sliding submatrix (k x k).

        Returns:
            List[List[int]]: A 2D matrix where each entry corresponds to the
            minimum absolute difference found in the respective k x k submatrix.
            If a submatrix has only one unique element, the difference is 0.
        """

        # Dimensions of the grid
        m, n = len(grid), len(grid[0])

        # Initialize result matrix with zeros.
        # Size: (m - k + 1) rows × (n - k + 1) columns
        res = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        # Iterate over all possible starting positions of k x k submatrices
        for i in range(m - k + 1):          # row start index
            for j in range(n - k + 1):      # column start index

                # Collect all elements inside the current k x k submatrix
                kgrid = []
                for x in range(i, i + k):   # iterate rows of submatrix
                    for y in range(j, j + k):  # iterate cols of submatrix
                        kgrid.append(grid[x][y])

                # Sort the elements to check consecutive differences
                kgrid.sort()

                # Initialize minimum difference as infinity
                kmin = float("inf")

                # Compare consecutive elements to find smallest difference
                for t in range(1, len(kgrid)):
                    # Skip duplicates (no difference between equal values)
                    if kgrid[t] == kgrid[t - 1]:
                        continue
                    # Update minimum difference
                    kmin = min(kmin, kgrid[t] - kgrid[t - 1])

                # If we found a valid difference, store it
                # Otherwise (all elements equal), leave as 0
                if kmin != float("inf"):
                    res[i][j] = kmin

        return res
