class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """
        Count Binary Substrings

        Problem:
        ----------
        Given a binary string `s` (consisting only of '0' and '1'), 
        we need to count the number of non-empty substrings that have:
            1. The same number of consecutive '0's and '1's.
            2. All '0's grouped together and all '1's grouped together.

        Example:
        ----------
        Input:  "00110011"
        Valid substrings: "0011", "01", "1100", "10", "0011", "01"
        Output: 6

        Approach:
        ----------
        - Instead of generating all substrings (which is inefficient),
          we track consecutive groups of identical characters.
        - For each group, the number of valid substrings depends on the 
          minimum length between the current group and the previous group.
          (Because a valid substring must balance equal consecutive 0s and 1s.)
        
        Steps:
        ----------
        1. Initialize:
           - `result` → total count of valid substrings.
           - `curr` → length of current consecutive group.
           - `prr` → length of previous consecutive group.
        
        2. Traverse the string:
           - If current char == previous char → increment `curr`.
           - Else (group changes):
               * Add `min(curr, prr)` to result (valid substrings formed).
               * Update `prr = curr` (previous group becomes current).
               * Reset `curr = 1` (new group starts).
        
        3. After loop ends:
           - Add `min(curr, prr)` one last time to account for the final group.
        
        Complexity:
        ----------
        - Time: O(n), single pass through the string.
        - Space: O(1), only counters used.

        Returns:
        ----------
        int → total number of valid binary substrings.
        """

        result = 0
        curr, prr = 1, 0  # curr = current group length, prr = previous group length

        # Traverse string starting from second character
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                # Same as previous → extend current group
                curr += 1
            else:
                # Group change → count valid substrings
                result += min(curr, prr)
                prr = curr  # update previous group length
                curr = 1    # reset current group length

        # Final addition for last group
        return result + min(curr, prr)
