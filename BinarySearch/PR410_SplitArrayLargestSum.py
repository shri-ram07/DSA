class Solution(object):
    def splitArray(self, nums, k):
        """
        Problem:
        --------
        Given an array 'nums' and an integer 'k', split the array into 'k' or fewer
        non-empty continuous subarrays such that the largest sum among these subarrays
        is minimized. Return that minimized largest sum.

        Example:
        --------
        nums = [7,2,5,10,8], k = 2
        Possible splits:
            [7,2,5] and [10,8] -> max sum = max(14,18) = 18
            [7,2] and [5,10,8] -> max sum = max(9,23) = 23
        The minimum possible largest sum is 18.

        Approach:
        ---------
        1. Use **Binary Search** on the answer space:
           - The minimum possible largest sum = max(nums) (since at least one subarray must contain the largest element).
           - The maximum possible largest sum = sum(nums) (if we take the whole array as one subarray).
        2. For each mid value in this range, check if we can split the array into <= k subarrays
           such that each subarray sum <= mid.
        3. If possible, shrink the search space (try smaller mid).
           Otherwise, increase mid.

        Time Complexity:
        ----------------
        - Binary search runs in O(log(sum(nums) - max(nums))).
        - For each mid, we scan the array once (O(n)).
        - Total: O(n log(sum(nums))).

        Space Complexity:
        -----------------
        - O(1) extra space (only counters and variables).

        ASCII Diagram of Binary Search:
        --------------------------------
        l = max(nums) ---------------------------- r = sum(nums)
                     |-----------|-----------|-----------|
                     mid1        mid2        mid3
        We check each mid:
            - If feasible -> move left (r = mid-1)
            - If not feasible -> move right (l = mid+1)
        Finally, 'res' stores the minimized largest sum.
        """

        def checkSum(m):
            """
            Helper function:
            ----------------
            Given a maximum allowed sum 'm', check if we can split
            nums into <= k subarrays such that each subarray sum <= m.
            """
            subarrays = 0   # count of subarrays formed
            curr = 0        # current subarray sum

            for x in nums:
                curr += x
                # If adding x exceeds allowed sum 'm',
                # start a new subarray
                if curr > m:
                    subarrays += 1
                    curr = x  # start new subarray with current element

            # After loop, we have subarrays+1 total subarrays
            return subarrays + 1 <= k

        # Binary search boundaries
        l, r = max(nums), sum(nums)
        res = r  # initialize result as maximum possible sum

        while l <= r:
            mid = (l + r) // 2  # candidate largest sum

            if checkSum(mid):
                # If feasible, update result and try smaller sum
                res = min(res, mid)
                r = mid - 1
            else:
                # If not feasible, increase allowed sum
                l = mid + 1

        return res
