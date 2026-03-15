MOD = 10**9 + 7

class Fancy:
    """
    Fancy Sequence (LeetCode 1622)

    This class implements a sequence that supports four operations:
    1. append(val): Add a new element to the end of the sequence.
    2. addAll(inc): Add 'inc' to every element in the sequence.
    3. multAll(m): Multiply every element in the sequence by 'm'.
    4. getIndex(idx): Return the element at index 'idx' modulo 1e9+7,
       or -1 if idx is out of bounds.

    Key Optimization:
    - Instead of updating the entire sequence for addAll/multAll (O(n)),
      we maintain two global parameters:
        * self.mul → current multiplication factor
        * self.add → current addition offset
    - When appending, we store a "normalized" value that undoes the
      current transformations using modular inverse.
    - When retrieving, we reconstruct the actual value by applying
      the global transformations back.
    - This makes all operations O(1).
    """

    def __init__(self):
        # Store normalized values of appended elements
        self.seq = []
        # Global multiplication factor (starts at 1, neutral element)
        self.mul = 1
        # Global addition offset (starts at 0)
        self.add = 0

    def append(self, val: int) -> None:
        """
        Append a new value to the sequence.
        We normalize it by undoing the current global transformations.
        Formula:
            stored = (val - add) * inv(mul) % MOD
        where inv(mul) is the modular inverse of mul.
        """
        inv = pow(self.mul, MOD - 2, MOD)  # Fermat's theorem for modular inverse
        stored = (val - self.add) * inv % MOD
        self.seq.append(stored)

    def addAll(self, inc: int) -> None:
        """
        Add 'inc' to all elements.
        Instead of looping, just update the global offset.
        """
        self.add = (self.add + inc) % MOD

    def multAll(self, m: int) -> None:
        """
        Multiply all elements by 'm'.
        Update both global multiplier and offset.
        """
        self.mul = (self.mul * m) % MOD
        self.add = (self.add * m) % MOD

    def getIndex(self, idx: int) -> int:
        """
        Retrieve the element at index 'idx'.
        Reconstruct the actual value:
            value = (stored[idx] * mul + add) % MOD
        """
        if idx >= len(self.seq):
            return -1
        return (self.seq[idx] * self.mul + self.add) % MOD
