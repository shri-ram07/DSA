class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        Merge Sorted Array (LeetCode #88)

        Problem:
        Given two sorted arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
        - nums1 has a size of m + n, where the first m elements are valid and the last n are placeholders (0s).
        - nums2 has n valid elements.

        Approach (Two-Pointer from the End):
        - Start filling nums1 from the back (index m+n-1).
        - Compare the last valid elements of nums1 and nums2.
        - Place the larger one at the end of nums1.
        - Move the pointer (m or n) backward accordingly.
        - If nums2 still has remaining elements, copy them into nums1.

        Why from the end?
        - Because nums1 has extra space at the end, starting from the back avoids overwriting useful values.

        Time Complexity:
        - O(m + n) → Each element is processed once.

        Space Complexity:
        - O(1) → In-place merge, no extra arrays used.

        Example:
        nums1 = [4,5,6,0,0,0], m = 3
        nums2 = [1,2,3], n = 3
        Output → [1,2,3,4,5,6]
        """

        # Pointer for the last index of merged array
        last = m + n - 1

        # Compare elements from the end of nums1 and nums2
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]  # Place larger element at the end
                m -= 1
            else:
                nums1[last] = nums2[n - 1]  # Place larger element at the end
                n -= 1
            last -= 1  # Move the "last" pointer backward

        # If nums2 still has elements left, copy them
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1

        # nums1 is modified in-place, no return needed
        return nums1


# Example usage
o = Solution()
result = o.merge([4,5,6,0,0,0], 3, [1,2,3], 3)
print(result)  # Output: [1,2,3,4,5,6]
