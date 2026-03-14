class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        """
        Generate the k-th lexicographical "happy string" of length n.

        A happy string is defined as:
        - Only containing characters 'a', 'b', 'c'.
        - No two consecutive characters are the same.
        - Strings are ordered lexicographically (dictionary order).

        Approach:
        ----------
        1. Use backtracking (DFS) to build all possible happy strings.
        2. Maintain a counter (`cnt`) to track how many valid strings have been generated.
        3. Once the counter reaches `k`, store the current string in `res`.
        4. Use `nonlocal` variables so that `cnt` and `res` can be updated across recursive calls.
        5. Backtracking ensures we explore all valid paths:
            - Append a character.
            - Recurse deeper.
            - Remove the character (`pop`) to restore state before trying the next option.
        6. Early exit: if `res` is already found, stop further recursion.

        Parameters:
        -----------
        n : int
            The desired length of the happy string.
        k : int
            The lexicographical index (1-based) of the happy string to return.

        Returns:
        --------
        str
            The k-th happy string if it exists, otherwise an empty string.
        """

        s = ['a', 'b', 'c']   # allowed characters
        res = ""              # result string (empty until found)
        cnt = 0               # counter for how many happy strings generated

        def solve(curr):
            nonlocal cnt, res
            # Base case: if current string length == n
            if len(curr) == n:
                cnt += 1
                if cnt == k:              # if this is the k-th string
                    res = ''.join(curr)   # store result
                return

            # Recursive case: try each character
            for ch in s:
                # Skip if same as last character (to maintain "happy" property)
                if curr and curr[-1] == ch:
                    continue

                curr.append(ch)   # choose
                solve(curr)       # recurse
                curr.pop()        # backtrack (undo choice)

                # Early stop: if result already found, no need to continue
                if res:
                    return

        solve([])   # start recursion with empty string
        return res
