class Solution:
    """
    Solution class for the LeetCode 'Add Binary' problem.
    This implementation simulates binary addition bit by bit,
    handling carries explicitly (like a full adder circuit).
    """

    def addBinary(self, a: str, b: str) -> str:
        """
        Add two binary strings and return their sum as a binary string.

        Args:
            a (str): First binary string (e.g., "1011").
            b (str): Second binary string (e.g., "1101").

        Returns:
            str: Binary string representing the sum of a and b.
        """

        # XOR helper: returns True if inputs differ, False if same
        def xor(a, b):
            return (a and not b) or (not a and b)

        # Full adder logic for one bit position
        def BitSum(i, j, carry):
            """
            Compute sum and carry for a single bit addition.

            Args:
                i (bool): Bit from string a (True for '1', False for '0').
                j (bool): Bit from string b.
                carry (bool): Carry-in from previous column.

            Returns:
                (bool, bool): (sum_bit, carry_out)
            """
            # Sum = i ⊕ j ⊕ carry
            addition = xor(xor(i, j), carry)

            # Carry-out = (i ∧ j) ∨ (carry ∧ (i ⊕ j))
            new_carry = (i and j) or (carry and xor(i, j))

            return addition, new_carry

        # Convert character '1'/'0' into boolean True/False
        def seeBinary(el):
            return el == '1'

        # Ensure 'a' is the longer string
        l1, l2 = len(a), len(b)
        if l1 < l2:
            return self.addBinary(b, a)

        carry = False   # initial carry is 0
        Sum = []        # collect sum bits here
        j = l2 - 1      # pointer for b (rightmost index)

        # Traverse from rightmost bit to leftmost
        for i in range(l1 - 1, -1, -1):
            el1 = seeBinary(a[i])                # bit from a
            el2 = seeBinary(b[j]) if j >= 0 else False  # bit from b (or 0 if exhausted)

            addition, carry = BitSum(el1, el2, carry)   # full adder step

            # Append sum bit ('1' if True else '0')
            Sum.append('1' if addition else '0')

            j -= 1  # move pointer left in b

        # If carry remains after final column, append it
        if carry:
            Sum.append('1')

        # Reverse collected bits to form final binary string
        return ''.join(reversed(Sum))
