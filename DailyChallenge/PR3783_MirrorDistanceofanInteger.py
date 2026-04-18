class Solution:
    def mirrorDistance(self, n: int) -> int:
        """
        Calculate the 'mirror distance' of an integer.

        The mirror distance is defined as the absolute difference between
        the original integer and its digit-reversed counterpart.

        Example:
            n = 123
            reversed = 321
            mirror distance = |123 - 321| = 198

        Args:
            n (int): The input integer whose mirror distance is to be calculated.

        Returns:
            int: The absolute difference between the integer and its reversed form.
        """
        # Convert the integer to a string so we can reverse its digits easily
        str_n = str(n)

        # Reverse the string using slicing [::-1]
        reversed_str = str_n[::-1]

        # Convert the reversed string back to an integer
        reversed_int = int(reversed_str)

        # Compute the absolute difference between the original and reversed integer
        distance = abs(n - reversed_int)

        # Return the computed mirror distance
        return distance
