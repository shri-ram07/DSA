# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        Find the first bad version using binary search.

        Args:
            n (int): The total number of versions (from 1 to n).

        Returns:
            int: The version number of the first bad version.

        Explanation:
            - We are given an API `isBadVersion(version)` that tells us if a version is bad.
            - Once a version is bad, all versions after it are also bad.
            - The goal is to minimize API calls and efficiently find the first bad version.
            - We use binary search to narrow down the range:
                * If mid is bad, the first bad version must be at mid or before → move right pointer.
                * If mid is good, the first bad version must be after mid → move left pointer.
            - Loop continues until left == right, which will be the first bad version.
        """

        # Initialize search boundaries
        l, r = 0, n

        # Binary search loop
        while l < r:
            mid = (l + r) // 2  # Find the middle version

            if isBadVersion(mid):  
                # If mid is bad, the first bad version is at mid or earlier
                r = mid
            else:
                # If mid is good, the first bad version must be after mid
                l = mid + 1

        # When loop ends, l == r → first bad version
        return l
