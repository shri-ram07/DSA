class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        """
        Check If a String Contains All Binary Codes of Size K
        -----------------------------------------------------

        Problem:
        ----------
        Given a binary string `s` and an integer `k`, determine if every possible 
        binary code (substring) of length `k` exists in `s`.

        Example:
        ----------
        Input: s = "00110110", k = 2
        Possible binary codes of length 2: {"00", "01", "10", "11"}
        Substrings of length 2 in s: {"00", "01", "11", "10"}
        Output: True (all codes are present)

        Approach:
        ----------
        1. The total number of distinct binary codes of length `k` is:
               possible_codes = 2^k
        2. Slide a window of size `k` across the string `s`.
        3. Store each substring of length `k` in a hash set.
        4. If the size of the set equals `2^k`, then all codes are present.

        Diagram (Sliding Window):
        ----------
        s = "00110110", k = 3

        Window positions:
        [001]10110   -> "001"
        0[011]0110   -> "011"
        00[110]110   -> "110"
        001[101]10   -> "101"
        0011[011]0   -> "011"
        00110[110]   -> "110"

        Distinct substrings collected in set:
        {"001", "011", "110", "101"} → size = 4

        Total possible codes of length 3 = 2^3 = 8
        Since 4 != 8 → return False

        Complexity:
        ----------
        - Time: O(n * k) in worst case (substring extraction + set insertion).
                But practically O(n), since slicing is optimized.
        - Space: O(2^k) for storing distinct substrings.

        Returns:
        ----------
        True  → if all binary codes of length k are present
        False → otherwise
        """

        # Edge case: if string length is smaller than k, impossible to contain all codes
        if len(s) < k:
            return False

        # Total possible binary codes of length k
        psbl = 2 ** k

        # Hash set to store unique substrings of length k
        HashForSubStringOFLenK = set()

        # Sliding window indices
        i, j = 0, k

        # Traverse string with window size k
        while j <= len(s):
            HashForSubStringOFLenK.add(s[i:j])  # Add substring to set
            i += 1
            j += 1

        # If we collected all possible codes, return True
        return len(HashForSubStringOFLenK) == psbl
