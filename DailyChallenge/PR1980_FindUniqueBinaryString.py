class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        """
        Find a binary string of length n that is not present in the given list.

        Problem Context:
        ----------------
        - Input: nums (List[str]) → list of binary strings, each of length n.
        - Goal: Return any binary string of length n that is NOT in nums.
        - Constraint: All strings in nums are unique.

        Approach:
        ---------
        1. Determine n (length of each binary string).
        2. Convert nums into a set for O(1) membership checks.
        3. Iterate through all possible binary numbers from 0 to 2^n - 1.
        4. For each integer x:
            - Convert x into a binary string of length n using `format(x, f'0{n}b')`.
              * `b` → binary format
              * `0{n}` → pad with leading zeros to ensure length n
            - Example: n=4, x=3 → "0011"
        5. If this candidate string is not in nums, return it immediately.

        Why This Works:
        ---------------
        - There are exactly 2^n possible binary strings of length n.
        - nums contains n unique strings, so at least one string is missing.
        - Iteration guarantees we will find a missing one.

        Complexity:
        -----------
        - Time: O(2^n) in worst case (iterating all candidates).
        - Space: O(n) for storing nums as a set.
        """

        n = len(nums[0])              # Length of each binary string
        nums = set(nums)              # Convert list to set for fast lookup
        max_int = int("1" * n, 2)     # Largest integer with n bits (e.g., "111" → 7)
        
        # Iterate through all possible binary numbers from 0 to max_int
        for x in range(max_int + 1):
            candidate = format(x, f'0{n}b')  # Binary string of length n, zero-padded
            if candidate not in nums:        # Found a missing string
                return candidate
