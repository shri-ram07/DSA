class Solution(object):
    def findMin(self, nums):
        """
        Find the minimum element in a rotated sorted array using binary search.

        Problem Context:
        ----------------
        A rotated sorted array is formed by taking a sorted array and rotating it 
        at some pivot. For example:
            Original sorted array: [1, 2, 3, 4, 5, 6, 7]
            Rotated version:       [4, 5, 6, 7, 1, 2, 3]

        Goal:
        -----
        Efficiently find the smallest element in such an array.

        Approach:
        ---------
        - Use binary search to reduce the search space.
        - At each step, compare the left, mid, and right values to decide 
          which half of the array contains the minimum.
        - Keep track of the minimum seen so far.

        ASCII Diagram (Rotation Example):
        ---------------------------------
        Suppose nums = [4, 5, 6, 7, 0, 1, 2]

        Indices:   0   1   2   3   4   5   6
        Values:   [4,  5,  6,  7,  0,  1,  2]
                   ^           ^           ^
                   l           mid         r

        Step 1: Compare nums[l] and nums[mid]
        Step 2: Decide whether to move left pointer (l) or right pointer (r)
        Step 3: Narrow down until the minimum is found.

        Time Complexity:
        ----------------
        O(log n) → Because we halve the search space each iteration.

        Space Complexity:
        -----------------
        O(1) → Only a few variables are used (l, r, mid, min_).

        Returns:
        --------
        int : The minimum element in the rotated sorted array.
        """

        # Initialize pointers
        l, r = 0, len(nums) - 1
        # Track minimum value seen so far
        min_ = float("inf")

        while l <= r:
            mid = (l + r) // 2  # Middle index

            # Case 1: Left half is sorted
            if nums[l] <= nums[mid]:
                # Minimum could be at nums[l]
                min_ = min(min_, nums[l])
                # Discard left half, move to right half
                l = mid + 1

            # Case 2: Right half is sorted
            elif nums[mid] <= nums[r]:
                # Minimum could be at nums[mid]
                min_ = min(min_, nums[mid])
                # Discard right half, move to left half
                r = mid - 1

        return min_
