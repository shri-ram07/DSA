class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        """
        Count numbers in the range [left, right] whose binary representation
        has a prime number of set bits (1s).

        Problem Context:
        ----------------
        - Each integer can be represented in binary.
        - The task is to count how many integers between 'left' and 'right'
          (inclusive) have a prime count of '1' bits in their binary form.

        Approach:
        ---------
        1. Predefine a set of prime numbers that could realistically occur
           as bit counts within the given range. For 32-bit integers, the
           maximum number of bits is 32, so primes up to 32 are sufficient.
        2. Iterate through each number in the range [left, right].
        3. Convert the number to binary using `bin(i)` and count the '1's.
        4. If the count of '1's is in the prime set, increment the counter.
        5. Return the final count.

        Example:
        --------
        left = 6, right = 10
        Binary forms:
        - 6  -> 110   -> 2 ones (prime)
        - 7  -> 111   -> 3 ones (prime)
        - 8  -> 1000  -> 1 one  (not prime)
        - 9  -> 1001  -> 2 ones (prime)
        - 10 -> 1010  -> 2 ones (prime)
        Result = 4
        """
        # Precomputed set of prime numbers up to 19 (covers typical bit counts).
        s = {2, 3, 5, 7, 11, 13, 17, 19}
        
        cnt = 0  # Initialize counter
        
        # Iterate through each number in the given range
        for i in range(left, right + 1):
            # Convert to binary string and count '1's
            count_ = str(bin(i)).count("1")
            
            # Check if the count of '1's is prime
            if count_ in s:
                cnt += 1  # Increment if prime
        
        return cnt
