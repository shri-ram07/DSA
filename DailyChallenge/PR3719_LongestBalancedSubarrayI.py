class Solution(object):
    def longestBalanced(self, nums):
        """
        Find the length of the longest balanced subarray.

        A subarray is considered balanced if it contains an equal number
        of distinct even and distinct odd elements. Duplicates within
        the subarray do not increase the distinct count.

        Parameters
        ----------
        nums : List[int]
            The input list of integers.

        Returns
        -------
        int
            The maximum length of a balanced subarray.
        """

        maxx = 0   # Stores the maximum balanced subarray length found
        n = len(nums)

        # Iterate over all possible starting indices of subarrays
        for x in range(n):
            seen = set()   # Track distinct elements in the current subarray
            even = 0       # Count of distinct even numbers
            odd = 0        # Count of distinct odd numbers

            # Expand the subarray from index x to y
            for y in range(x, n):
                # Only count distinct elements once
                if nums[y] not in seen:
                    seen.add(nums[y])
                    if nums[y] % 2 == 0:
                        even += 1
                    else:
                        odd += 1

                # Check if the current subarray is balanced
                if even == odd:
                    maxx = max(maxx, y - x + 1)

        return maxx
