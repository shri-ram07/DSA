class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Reverse the bits of a 32-bit unsigned integer.

        This implementation uses helper functions to:
        1. Convert the integer into a 32-bit binary string.
        2. Reverse the binary string.
        3. Convert the reversed binary string back into an integer.

        While this approach is more verbose than a bitwise method,
        it demonstrates step-by-step logic for:
        - Decimal to binary conversion
        - Padding to 32 bits
        - String reversal
        - Binary-to-decimal conversion using a dictionary of powers of two

        Example:
        --------
        Input:  n = 43261596
        Binary: 00000010100101000001111010011100
        Output: 964176192
        Binary: 00111001011110000010100101000000

        Parameters:
        -----------
        n : int
            A 32-bit unsigned integer.

        Returns:
        --------
        int
            The integer whose binary representation is the reverse of `n`.

        Notes:
        ------
        - This solution uses string manipulation and a dictionary of powers of two.
        - It is less efficient than a pure bitwise approach but is useful for
          educational purposes and understanding the mechanics of binary conversion.
        """

        # Edge case: if input is 0, reversed result is also 0
        if n == 0:
            return 0

        # HashMap stores powers of two for quick lookup
        # Example: {0:1, 1:2, 2:4, ..., 31:2**31}
        HashMap = {}
        for i in range(32):
            HashMap[i] = 2**i

        def convertTo32Binary(n: int) -> str:
            """
            Convert an integer into a 32-bit binary string.

            Steps:
            ------
            - Perform repeated division by 2 to extract remainders (binary digits).
            - Append digits to a list.
            - Pad with zeros until length is 32.
            - Return the binary string representation.
            """
            quotient = n // 2
            remainder = n % 2
            st = [str(remainder)]  # Start with least significant bit

            # Continue dividing until quotient becomes 1
            while quotient != 1:
                quotient, remainder = quotient // 2, quotient % 2
                st.append(str(remainder))

            # Append the final quotient (either 1 or 0)
            st.append(str(quotient))

            # Pad with zeros to ensure 32-bit length
            for _ in range(32 - len(st)):
                st.append(str(0))

            return ''.join(st)

        def convertToInteger(x: str) -> int:
            """
            Convert a binary string into its integer value.

            Steps:
            ------
            - Iterate over each bit in the string.
            - If the bit is '1', add the corresponding power of two from HashMap.
            - Return the accumulated integer result.
            """
            result = 0
            for m, n in HashMap.items():
                if x[m] == "1":
                    result += n
            return result

        # Convert to 32-bit binary string, reverse it, then convert back to integer
        return convertToInteger(convertTo32Binary(n)[::-1])
