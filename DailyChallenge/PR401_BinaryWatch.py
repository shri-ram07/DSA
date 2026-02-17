from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        """
        Generate all possible times on a binary watch given a specific number of LEDs turned on.

        A binary watch has:
        - 4 LEDs to represent the hour (0–11).
        - 6 LEDs to represent the minutes (0–59).
        Each LED corresponds to a bit in the binary representation of the number.

        The task:
        - Count how many LEDs (bits) are ON for each possible hour and minute.
        - If the total number of ON bits equals `turnedOn`, that time is valid.
        - Return all valid times in "H:MM" format (with leading zero for minutes < 10).

        Parameters
        ----------
        turnedOn : int
            The number of LEDs that are turned on.

        Returns
        -------
        List[str]
            A list of strings representing all possible valid times.
            Example: ["3:07", "8:23", "11:59"]

        Notes
        -----
        - We manually implement bit counting logic (instead of using Python built-ins like bin(n).count("1")),
          to understand how binary decomposition works.
        - The algorithm uses a hashmap (dictionary) to store precomputed bit counts for numbers 0–59,
          so we don’t repeatedly calculate them.
        - Time complexity: O(12 * 60) = O(720), which is efficient enough.
        """

        def countSetBits(n: int) -> int:
            """
            Count the number of set bits (1s) in the binary representation of n.

            Logic:
            - While n > 0:
                - Check the least significant bit (LSB) using modulus (% 2).
                - If LSB == 1, increment count.
                - Divide n by 2 (integer division) to shift right.
            - Continue until n becomes 0.

            Example:
            n = 7 (binary 111)
            Iteration 1: remainder=1 → count=1, n=3
            Iteration 2: remainder=1 → count=2, n=1
            Iteration 3: remainder=1 → count=3, n=0
            Result = 3
            """
            cnt = 0
            while n > 0:
                if n % 2 == 1:   # If LSB is 1, increment count
                    cnt += 1
                n = n // 2       # Shift right by dividing by 2
            return cnt

        # Precompute bit counts for all numbers 0–59 (covers both minutes and hours).
        HashMap = {i: countSetBits(i) for i in range(60)}

        result = []
        # Iterate over all possible hours (0–11)
        for i in range(12):
            s1 = HashMap[i]  # Number of LEDs ON for this hour
            # Iterate over all possible minutes (0–59)
            for j in range(60):
                s2 = HashMap[j]  # Number of LEDs ON for this minute
                # If total LEDs ON equals turnedOn, it's a valid time
                if s1 + s2 == turnedOn:
                    # Format minutes with leading zero if < 10
                    result.append(f"{i}:{j:02d}")
                # Optimization: if sum exceeds turnedOn, break early
                elif s1 + s2 > turnedOn:
                    break
        return result
