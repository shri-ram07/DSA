class Solution:
    def minOperations(self, s: str) -> int:
        """
        Optimal version:
        ----------------
        Directly compare each character with expected values for both patterns.
        Avoids building extra strings → O(1) space.
        """
        n = len(s)
        cnt1 = 0  # flips if alternating starts with '0'
        cnt2 = 0  # flips if alternating starts with '1'

        for i in range(n):
            expected1 = '0' if i % 2 == 0 else '1'
            expected2 = '1' if i % 2 == 0 else '0'

            if s[i] != expected1:
                cnt1 += 1
            if s[i] != expected2:
                cnt2 += 1

        return min(cnt1, cnt2)
