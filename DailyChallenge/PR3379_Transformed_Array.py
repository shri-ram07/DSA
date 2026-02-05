class Solution(object):
    def constructTransformedArray(self, nums):
        """
        Construct a transformed array from a circular list.

        The idea:
        ----------
        Each element in `nums` tells us how many steps to move forward (positive)
        or backward (negative) from its current index in a circular array.
        We then take the value at the new index and place it into the result array.

        Formula:
        --------
        new_index = (i + nums[i]) % n

        - i        : current index
        - nums[i]  : step size (can be positive, negative, or zero)
        - n        : length of the array
        - % n      : ensures wrapping around (circular behavior)

        Why modulo works:
        -----------------
        Modulo ensures that the index always stays within [0, n-1].
        - If we go past the end, it wraps back to the start.
        - If we go before the start (negative index), Python’s % operator
          wraps it correctly into the valid range.

        ASCII Diagram (example with n = 4):
        -----------------------------------
        nums = [3, -2, 1, 1]

        Index positions (circular):
        
              [0] → [1] → [2] → [3]
               ↑                   ↓
               └───────────────────┘

        Walkthrough:
        - At i=0, nums[0]=3 → new_index = (0+3)%4 = 3 → result[0] = nums[3]
        - At i=1, nums[1]=-2 → new_index = (1-2)%4 = -1%4 = 3 → result[1] = nums[3]
        - At i=2, nums[2]=1 → new_index = (2+1)%4 = 3 → result[2] = nums[3]
        - At i=3, nums[3]=1 → new_index = (3+1)%4 = 0 → result[3] = nums[0]

        Final result = [nums[3], nums[3], nums[3], nums[0]] = [1, 1, 1, 3]

        Returns:
        --------
        A new list `result` of length n, where each element is determined
        by traversing the circular list according to nums[i].
        """

        n = len(nums)              # Length of the input array
        result = []                # Initialize empty result list

        # Traverse each index of nums
        for i in range(n):
            # Compute the new index using modulo arithmetic
            # (i + nums[i]) ensures movement forward/backward
            # % n ensures wrapping around the circular list
            new_index = (i + nums[i]) % n

            # Append the element at the new index into result
            result.append(nums[new_index])

        return result              # Return the transformed array
