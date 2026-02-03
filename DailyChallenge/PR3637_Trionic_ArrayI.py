class Solution(object):
    def isTrionic(self, nums):
        """
        Determine if an array is 'Trionic'.

        A 'Trionic' array must follow this exact 3-phase pattern:
        1. Strictly Increasing (at least one step)
        2. Strictly Decreasing (at least one step)
        3. Strictly Increasing again (at least one step)

        The array must end exactly at the end of phase 3.
        Length must be >= 4 to allow all three phases.

        Example:
        nums = [1, 3, 5, 4, 2, 6]
        - Phase 1: 1 → 3 → 5   (increasing)
        - Phase 2: 5 → 4 → 2   (decreasing)
        - Phase 3: 2 → 6       (increasing)
        => Valid Trionic → returns True
        """

        n = len(nums)
        l = 0

        # -------------------------------
        # Phase 1: Strictly Increasing ↑
        # -------------------------------
        # Keep moving forward while next element is larger
        while l < n-2 and nums[l] < nums[l+1]:
            l += 1

        # If no increase happened (l == 0) or we reached the end too early
        if l == n-1 or l == 0:
            return False

        p = l  # mark the peak index

        # -------------------------------
        # Phase 2: Strictly Decreasing ↓
        # -------------------------------
        while l < n-1 and nums[l] > nums[l+1]:
            l += 1

        # If no decrease happened (l == p) or we ended too early
        if l == n-1 or l == p:
            return False

        # -------------------------------
        # Phase 3: Strictly Increasing ↑
        # -------------------------------
        while l < n-1 and nums[l] < nums[l+1]:
            l += 1

        # If we reached the end exactly after phase 3 → valid
        if l == n-1:
            return True

        # Otherwise, invalid
        return False
