class Solution:
    def binaryGap(self, n: int) -> int:
        """
        Calculate the maximum distance (gap) between two consecutive '1's 
        in the binary representation of a given integer.

        The binary gap is defined as the number of positions between 
        two successive '1' bits in the binary string of `n`. 
        For example:
            - n = 22 (binary: '10110') → gaps are [2, 1], max gap = 2
            - n = 8  (binary: '1000')  → only one '1', max gap = 0
            - n = 5  (binary: '101')   → gap = 2

        Approach:
        1. Convert the integer to its binary representation (without '0b' prefix).
        2. Iterate through the binary string using `enumerate` to track indices.
        3. Keep track of the last index where '1' was seen (`prev`).
        4. When another '1' is found, compute the distance from `prev` and update `max_gap`.
        5. Return the maximum gap found. If fewer than two '1's exist, return 0.

        Time Complexity: O(k), where k = number of bits in n.
        Space Complexity: O(1), since only a few variables are used.

        Parameters:
        ----------
        n : int
            The input integer whose binary gap is to be calculated.

        Returns:
        -------
        int
            The maximum gap between consecutive '1's in the binary representation.
        """

        # Step 1: Convert integer to binary string (remove '0b' prefix)
        s = bin(n)[2:]

        # Step 2: Initialize variables
        prev = -1       # Stores index of last '1' encountered
        max_gap = 0     # Stores maximum gap found

        # Step 3: Iterate through binary string
        for i, bit in enumerate(s):
            if bit == "1":  # Found a '1'
                if prev != -1:  # If there was a previous '1'
                    # Step 4: Calculate gap and update max_gap
                    max_gap = max(max_gap, i - prev)
                # Update prev to current index
                prev = i

        # Step 5: Return result
        return max_gap
