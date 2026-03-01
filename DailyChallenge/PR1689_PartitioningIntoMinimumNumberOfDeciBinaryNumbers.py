class Solution:
    def minPartitions(self, n: str) -> int:
        """
        Problem:
        --------
        Given a string `n` representing a positive decimal integer, 
        return the minimum number of deci-binary numbers needed to sum up to `n`.

        A deci-binary number is defined as a number where each digit is either 0 or 1.
        For example: 101, 110, 1111 are deci-binary numbers.

        Key Insight:
        ------------
        - Each digit in `n` must be formed by stacking 1s from different deci-binary numbers.
        - If a digit is '7', you need at least 7 deci-binary numbers (each contributing a '1' in that place).
        - Therefore, the minimum number of deci-binary numbers required is simply the maximum digit in `n`.

        Example:
        --------
        Input: n = "82734"
        Digits: 8, 2, 7, 3, 4
        Maximum digit = 8
        Output: 8

        Explanation:
        - To form '8' in the first position, we need at least 8 deci-binary numbers.
        - Other digits (2, 7, 3, 4) require fewer, but the maximum dominates.

        Time Complexity:
        ----------------
        O(len(n)) → We scan through the string once to find the maximum digit.

        Space Complexity:
        -----------------
        O(1) → We only store the maximum digit.

        Parameters:
        -----------
        n : str
            A string representing a positive integer (up to 10^5 digits).

        Returns:
        --------
        int
            The minimum number of deci-binary numbers required.
        """

        # Step 1: Find the maximum digit in the string `n`
        # `max(n)` returns the largest character (digit) in the string
        # Convert it to integer since `max(n)` gives a string
        return int(max(n))
