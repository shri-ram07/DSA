class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        Find the median of two sorted arrays using binary search.

        Problem:
        --------
        Given two sorted arrays nums1 and nums2, find the median of the two arrays.
        The median is the "middle value" when the arrays are combined and sorted.
        If the total length is odd → median is the middle element.
        If the total length is even → median is the average of the two middle elements.

        Naive approach:
        ---------------
        Merge both arrays and sort → O((m+n) log(m+n)) time.
        Too slow for large inputs.

        Efficient approach (Binary Search Partition):
        ---------------------------------------------
        We want to partition both arrays into LEFT and RIGHT halves such that:
            max(Left) <= min(Right)
        Once this condition is satisfied, the median can be found from boundary values.

        Key idea:
        ---------
        - Perform binary search on the smaller array (nums1).
        - Partition nums1 at index Px, then partition nums2 at Py so that:
              Px + Py = (m + n + 1) // 2
          (ensures left half has the correct number of elements).
        - Define boundary values:
              x1 = max element on left of nums1 partition
              x2 = max element on left of nums2 partition
              x3 = min element on right of nums1 partition
              x4 = min element on right of nums2 partition
        - If x1 <= x4 and x2 <= x3 → correct partition found.
          Median = (max(x1, x2) + min(x3, x4)) / 2 if even length
                 = max(x1, x2) if odd length.

        ASCII Diagram:
        --------------
        Example: nums1 = [1, 3], nums2 = [2]

        Combined sorted array = [1, 2, 3]
        Median = 2

        Binary search partitions:

        nums1: [1 | 3]   Px = 1
        nums2: [2 | ]    Py = 1

        Left side = [1, 2]
        Right side = [3]

        Condition satisfied: max(left)=2, min(right)=3
        Median = 2

        Complexity:
        -----------
        - Time: O(log(min(m, n))) because we binary search only on the smaller array.
        - Space: O(1)

        Returns:
        --------
        Float value representing the median of the two arrays.
        """

        m, n = len(nums1), len(nums2)

        # Ensure nums1 is the smaller array (binary search is cheaper on smaller one)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        l, r = 0, m
        while l <= r:
            # Partition index for nums1
            Px = (l + r) // 2
            # Partition index for nums2 (balance left and right halves)
            Py = (m + n + 1) // 2 - Px

            # Boundary values (handle edges with -inf / +inf)
            x1 = nums1[Px-1] if Px > 0 else float('-inf')   # left of nums1
            x2 = nums2[Py-1] if Py > 0 else float('-inf')   # left of nums2
            x3 = nums1[Px] if Px < m else float('inf')      # right of nums1
            x4 = nums2[Py] if Py < n else float('inf')      # right of nums2

            # Check if partition is valid
            if x1 <= x4 and x2 <= x3:
                # If total length is even → median is average of two middle values
                if (m+n) % 2 == 0:
                    return (max(x1, x2) + min(x3, x4)) / 2.0
                # If total length is odd → median is max of left side
                else:
                    return max(x1, x2)

            # If left side of nums1 is too big, move partition left
            elif x1 > x4:
                r = Px - 1
            # If left side of nums2 is too big, move partition right
            else:
                l = Px + 1

        # Should never reach here if inputs are valid
        return -1
