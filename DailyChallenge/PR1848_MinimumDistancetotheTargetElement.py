from typing import List

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        """
        Find the minimum distance between the given start index and any index 
        in the list `nums` where the value equals `target`.

        Parameters
        ----------
        nums : List[int]
            The list of integers to search through.
        target : int
            The integer value we want to locate in `nums`.
        start : int
            The reference index from which distances are measured.

        Returns
        -------
        int
            The smallest absolute difference between `start` and any index `i` 
            such that nums[i] == target.

        Approach
        --------
        1. Initialize `curr` as infinity to represent the minimum distance found so far.
        2. Iterate through all indices of `nums`.
        3. Whenever nums[i] equals target:
            - Compute the absolute distance between `start` and `i`.
            - If this distance is smaller than the current minimum, update `curr`.
        4. Return the final minimum distance.

        Example
        -------
        >>> sol = Solution()
        >>> sol.getMinDistance([1,2,3,4,5], target=5, start=3)
        1
        (Because nums[4] == 5 and |3-4| = 1)
        """
        # Initialize minimum distance as infinity
        curr = float("inf")

        # Traverse the list to check each element
        for i in range(len(nums)):
            # If the current element matches the target
            if nums[i] == target:
                # Calculate distance from start index
                distance = abs(start - i)
                # Update minimum distance if smaller
                if distance < curr:
                    curr = distance

        # Return the smallest distance found
        return curr
