class Solution(object):
    def findPeakElement(self, nums):
        """
        Find Peak Element
        -----------------
        A "peak" element is one that is strictly greater than its neighbors.
        - For index i: nums[i] > nums[i-1] and nums[i] > nums[i+1].
        - Edge cases: 
            * If i = 0, only check nums[0] > nums[1].
            * If i = n-1, only check nums[n-1] > nums[n-2].

        This function uses **binary search** to find *any* peak element.

        Logic:
        ------
        1. Start with two pointers:
            l = 0 (left boundary)
            r = len(nums) - 1 (right boundary)

        2. While l < r:
            - Compute mid = (l + r) // 2
            - Compare nums[mid] with nums[mid+1]:
                * If nums[mid] < nums[mid+1]:
                    → slope is rising, so peak must be on the right
                    → move l = mid + 1
                * Else:
                    → slope is falling, so peak is on the left (or at mid)
                    → move r = mid

        3. When l == r, both pointers meet at a peak index.

        Diagram (mountain analogy):
        ---------------------------
        Imagine the array as a mountain range:

            nums = [1, 2, 3, 1]
                     ^
                     Peak (3 is greater than both neighbors)

        Binary search works like climbing:
        - If slope goes up (nums[mid] < nums[mid+1]), move right.
        - If slope goes down (nums[mid] > nums[mid+1]), move left.
        - Eventually, you stop at the summit (the peak).

        Example Dry Run:
        ----------------
        nums = [1, 2, 3, 1]
        l=0, r=3
        mid=1 → nums[1]=2 < nums[2]=3 → move right → l=2
        mid=2 → nums[2]=3 > nums[3]=1 → move left → r=2
        l=r=2 → return 2 (peak index)

        Complexity:
        ------------
        - Time: O(log n) because we halve the search space each step.
        - Space: O(1) since we only use a few pointers.
        """

        # Initialize left and right boundaries
        l, r = 0, len(nums) - 1

        # Special case: if only one element, it's trivially a peak
        if len(nums) == 1:
            return 0

        # Binary search loop
        while l < r:
            mid = (l + r) // 2  # middle index

            # If slope is rising, peak must be on the right
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                # If slope is falling, peak is on the left (or at mid)
                r = mid

        # When l == r, we've found a peak
        return l
