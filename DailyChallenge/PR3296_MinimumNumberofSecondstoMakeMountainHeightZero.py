import math
from typing import List

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        """
        Calculate the minimum number of seconds required to reduce a mountain of given height to zero
        using multiple workers with different time efficiencies.

        Each worker with time `t` can reduce the mountain in increasing chunks:
        - 1 unit in `t` seconds
        - 2 units in `2t` seconds
        - 3 units in `3t` seconds
        - ...
        So in `mid` seconds, a worker can reduce at most `k` units where:
            t * (k*(k+1)//2) <= mid
        (This is derived from the sum of the first k natural numbers.)

        The algorithm uses binary search to find the smallest `mid` such that
        the total reduction across all workers is >= mountainHeight.

        Args:
            mountainHeight (int): The total height of the mountain to be reduced.
            workerTimes (List[int]): List of worker times, where each value represents
                                     the time taken by that worker to reduce 1 unit.

        Returns:
            int: The minimum number of seconds required to reduce the mountain to zero.
        """

        def check(mid: int) -> bool:
            """
            Check if the mountain can be reduced to zero (or below) within `mid` seconds.

            For each worker, compute the maximum number of units they can reduce in `mid` seconds
            using the quadratic formula:
                k = floor((-1 + sqrt(1 + 8*mid/t)) / 2)

            Args:
                mid (int): Candidate number of seconds.

            Returns:
                bool: True if total reduction >= mountainHeight, False otherwise.
            """
            h = 0  # total units reduced by all workers
            for t in workerTimes:
                # Compute maximum k units this worker can reduce in `mid` seconds
                k = int((-1 + math.isqrt(1 + 8 * mid // t)) // 2)
                h += k
            return h >= mountainHeight

        # Binary search boundaries:
        # l = minimum possible time (1 second)
        # r = worst-case time (slowest worker doing all work sequentially)
        l = 1
        r = max(workerTimes) * (mountainHeight * (mountainHeight + 1) // 2)

        # Binary search loop
        while l <= r:
            mid = (r + l) // 2
            if check(mid):
                # If possible within mid seconds, try smaller time
                r = mid - 1
            else:
                # Otherwise, increase time
                l = mid + 1

        # l will be the smallest valid time
        return l
