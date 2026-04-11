from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        """
        Find the minimum distance between three equal elements in an array.

        Problem Context:
        ----------------
        Given an array `nums`, we want to find the minimum possible distance
        defined as:
            distance = 2 * (index_of_third_occurrence - index_of_first_occurrence)
        for any triplet of equal elements.

        If no element occurs at least three times, return -1.

        Approach:
        ---------
        1. Use a dictionary (MAP) to store indices of each number.
           - Keys: unique numbers in nums
           - Values: list of indices where the number appears
        2. Iterate through nums:
           - Append the current index to the list for nums[i].
           - If the list length >= 3, check the last 3 occurrences.
           - Compute distance using the formula:
                 2 * (li[-1] - li[-3])
             where li[-1] is the latest index and li[-3] is the third‑last index.
           - Update `minn` with the minimum distance found so far.
        3. Return `minn` if updated, else return -1.

        Time Complexity:
        ----------------
        O(n), where n = len(nums), since we traverse the array once.

        Space Complexity:
        -----------------
        O(k), where k = number of distinct elements in nums,
        each storing at most all indices (can be optimized to last 3 only).
        """

        # Initialize dictionary with empty lists for each unique number
        MAP = {num: [] for num in set(nums)}

        # Start with infinity as the minimum distance
        minn = float("inf")

        # Traverse the array
        for i in range(len(nums)):
            # Append current index to the list of occurrences for nums[i]
            MAP[nums[i]].append(i)

            # If we have at least 3 occurrences of nums[i]
            if len(MAP[nums[i]]) >= 3:
                li = MAP[nums[i]]
                # Compute distance using the last and third‑last index
                distance = 2 * (li[-1] - li[-3])
                # Update minimum distance
                minn = min(minn, distance)

        # If no valid triplet found, return -1
        return minn if minn != float("inf") else -1
