from typing import List

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        """
        Find the shortest circular distance from a given start index to any occurrence 
        of the target string in the list of words.

        Problem Context:
        ----------------
        - You are given a circular array of strings (`words`).
        - You start at index `startIndex`.
        - You want to find the minimum number of steps (forward or backward) 
          required to reach any occurrence of `target`.

        Parameters:
        -----------
        words : List[str]
            The list of words arranged in a circular manner.
        target : str
            The word we want to reach.
        startIndex : int
            The index from which we start moving.

        Returns:
        --------
        int
            The minimum number of steps required to reach the target word.
            Returns -1 if the target word does not exist in the list.

        Approach:
        ---------
        - Iterate through the list to find all indices where `words[i] == target`.
        - For each occurrence, compute:
            * Forward distance: (i - startIndex + n) % n
            * Backward distance: (startIndex - i + n) % n
        - Take the minimum of forward and backward distances.
        - Keep track of the smallest distance across all occurrences.
        - If no occurrence is found, return -1.
        """

        dis = float("inf")  # Initialize minimum distance as infinity

        for i in range(len(words)):
            if words[i] == target:  # Found an occurrence of target
                # Compute forward distance (clockwise movement)
                forward = (i - startIndex + len(words)) % len(words)
                # Compute backward distance (counter-clockwise movement)
                backward = (startIndex - i + len(words)) % len(words)
                # Update minimum distance with the smaller of forward/backward
                dis = min(dis, min(forward, backward))

        # If dis was updated, return it; otherwise return -1 (target not found)
        return dis if dis != float("inf") else -1
