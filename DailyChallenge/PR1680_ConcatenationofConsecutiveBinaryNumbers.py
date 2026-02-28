class Solution:
    def concatenatedBinary(self, n: int) -> int:
        """
        Concatenation of Consecutive Binary Numbers (Efficient Bit Manipulation)

        Problem:
            Concatenate binary representations of numbers from 1 to n.
            Return the decimal value modulo (10^9 + 7).

        Approach:
            - Instead of building a giant string, we update the result iteratively.
            - For each i:
                1. Find how many bits i has (i.bit_length()).
                2. Shift the current result left by that many bits (multiply by 2^length).
                3. Add i to the result.
                4. Apply modulo to keep the number bounded.

        Why Bit Shifting?
            - Shifting left by k bits is equivalent to multiplying by 2^k.
            - This makes space for the new binary digits before appending i.
            - Much faster and memory-efficient than string concatenation.

        Parameters:
            n (int): Upper bound of sequence (1 ≤ n ≤ 10^5).

        Returns:
            int: Decimal value of concatenated binary string modulo (10^9 + 7).

        Example Dry Run (n=3):
            i=1 → result = 1
            i=2 → result = (1 << 2) + 2 = 6
            i=3 → result = (6 << 2) + 3 = 27
            Output = 27
        """
        MOD = 10**9 + 7
        result = 0

        for i in range(1, n + 1):
            length = i.bit_length()  # number of bits in i
            result = ((result << length) + i) % MOD

        return result
