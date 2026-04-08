class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        """
        Apply a series of range-based multiplication queries on an array,
        then compute the XOR of all elements in the modified array.

        Parameters
        ----------
        nums : List[int]
            The initial array of integers.
        queries : List[List[int]]
            A list of queries, where each query is defined as:
            [l, r, k, v]
            - l : int
                Starting index of the range (inclusive).
            - r : int
                Ending index of the range (inclusive).
            - k : int
                Step size for selecting indices within [l, r].
            - v : int
                Multiplier applied to each selected element.

        Returns
        -------
        int
            The XOR of all elements in the array after applying
            all queries. The XOR operation is performed bitwise
            across the entire array.

        Notes
        -----
        - Multiplication results are taken modulo 10^9 + 7 to
          prevent integer overflow and keep values bounded.
        - XOR is useful here because it acts like a parity check:
          elements that appear an even number of times cancel out,
          while odd occurrences remain in the final result.
        """

        MOD = 10**9 + 7  # Large prime modulus to keep values bounded

        # Process each query one by one
        for i in queries:
            l, r, k, v = i  # unpack query parameters
            # Iterate through indices from l to r, stepping by k
            while l <= r:
                # Multiply the element by v and take modulo
                nums[l] = (nums[l] * v) % MOD
                l += k  # move to the next index in step size k

        # After applying all queries, compute XOR of the entire array
        result = 0
        for x in nums:
            result ^= x  # XOR accumulates across all elements

        return result
