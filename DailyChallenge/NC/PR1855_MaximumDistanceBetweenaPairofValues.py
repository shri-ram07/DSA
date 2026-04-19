from typing import List

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Find the maximum distance between a valid pair (i, j).

        A pair is valid if:
        - i <= j
        - nums1[i] <= nums2[j]

        Args:
            nums1 (List[int]): First non-increasing array
            nums2 (List[int]): Second non-increasing array

        Returns:
            int: Maximum distance j - i among valid pairs
        """
        i, j = 0, 0
        maxDist = 0

        # Two-pointer traversal
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                # Valid pair, update max distance
                maxDist = max(maxDist, j - i)
                j += 1
            else:
                # nums1[i] too large, move i forward
                i += 1

        return maxDist
