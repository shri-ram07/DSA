class Solution:
    def bitwiseComplement(self, n: int) -> int:
        """
        Compute the bitwise complement of a given non-negative integer.

        The bitwise complement of an integer `n` is obtained by flipping all bits
        in its binary representation (excluding leading zeros). For example:
        - Input: 5 (binary "101")
        - Output: 2 (binary "010")

        Steps:
        1. Convert the integer `n` to its binary string representation.
        2. Flip each bit ('1' becomes '0', '0' becomes '1').
        3. Convert the flipped binary string back to an integer.
        
        Args:
            n (int): A non-negative integer whose bitwise complement is required.
        
        Returns:
            int: The bitwise complement of `n`.
        """

        def invert(s: str) -> str:
            """Helper function to flip a single binary digit."""
            if s == "1":
                return "0"
            else:
                return "1"

        # Convert integer to binary string (without '0b' prefix)
        binary = str(bin(n))[2:]

        # Flip each bit using the helper function
        new_str = ""
        for i in binary:
            new_str += invert(i)

        # Convert flipped binary string back to integer
        return int(new_str, 2)
