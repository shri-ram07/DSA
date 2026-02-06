class Solution(object):
    def minRemoval(self, nums, k):
        """
        Problem:
        --------
        Given an array of numbers (nums) and a multiplier (k),
        we want to remove the minimum number of elements so that
        the remaining array is "balanced".
        
        Balanced means:
            max_element <= k * min_element
        i.e. the largest number in the subarray should not be more than
        k times the smallest number.

        Approach:
        ---------
        1. Sort the array first.
           - Sorting helps because once the array is ordered,
             the smallest and largest values in any subarray
             are easy to find (just look at the ends).
        
        2. Use a sliding window (two pointers: l and r).
           - 'l' points to the left boundary (smallest element in the window).
           - 'r' moves forward one step at a time (expanding the window).
           - If the condition nums[r] <= nums[l] * k is violated,
             we move 'l' forward until the window becomes valid again.
        
        3. Track the maximum window size (max_len).
           - This represents the largest balanced subarray we can keep.
        
        4. Answer = total length - max_len
           - Because we want to remove the minimum number of elements,
             we keep the largest valid subarray and remove the rest.

        Example:
        --------
        nums = [1, 34, 23], k = 2
        Sorted nums = [1, 23, 34]
        - Largest balanced subarray is [23, 34] (since 34 <= 2*23).
        - Length of this subarray = 2
        - Total length = 3
        - Minimum removals = 3 - 2 = 1

        Complexity:
        -----------
        Time Complexity:
            - Sorting: O(n log n)
            - Sliding window: O(n) (each element visited at most twice)
            - Total: O(n log n), which is optimal for this problem.
        
        Space Complexity:
            - O(1) extra space (sorting is in-place, only a few variables used).

        Human-friendly summary:
        -----------------------
        Think of it like this:
        - First, line up the numbers in order.
        - Then, stretch a window across them as far as possible
          while keeping the "largest <= k * smallest" rule.
        - The biggest window you can stretch is the part you keep.
        - Everything outside that window gets removed.
        - The fewer you remove, the better — so we subtract the window size
          from the total size to get the minimum removals.
        """

        # Step 1: Sort the array so we can easily check min/max in order
        nums.sort()
        n = len(nums)

        # Step 2: Initialize left pointer and max window length
        l = 0
        max_len = 0

        # Step 3: Expand the right pointer one step at a time
        for r in range(n):
            # If condition breaks (too large compared to smallest),
            # move left pointer forward until it's valid again
            while nums[r] > nums[l] * k:
                l += 1
            # Update the largest valid window size
            max_len = max(max_len, r - l + 1)

        # Step 4: Minimum removals = total length - largest valid window
        return n - max_len
