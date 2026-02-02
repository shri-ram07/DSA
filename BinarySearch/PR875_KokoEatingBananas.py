import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        Problem:
        --------
        Koko loves bananas. She has 'piles' of bananas and wants to eat them all within 'h' hours.
        Each hour she chooses a pile and eats 'k' bananas from it. If the pile has fewer than 'k',
        she eats the whole pile. We need to find the minimum eating speed 'k' such that she can
        finish all piles within 'h' hours.

        Approach:
        ---------
        - We use **Binary Search** on the possible eating speeds.
        - The minimum speed is 1 (slowest possible).
        - The maximum speed is max(piles) (fastest possible, eat a whole pile in one hour).
        - For each candidate speed 'mid', we calculate how many hours it would take to eat all piles.
        - If hours <= h, then 'mid' is a valid speed, but we try smaller speeds (search left).
        - If hours > h, then 'mid' is too slow, so we try larger speeds (search right).
        - The answer is the smallest speed that allows finishing within 'h' hours.

        ASCII Diagram of Binary Search:
        --------------------------------
        l = 1                                r = max(piles)
        |-------------------------------------|
                        mid
        If hours(mid) <= h → move left (r = mid - 1)
        If hours(mid) > h  → move right (l = mid + 1)

        Example:
        piles = [30,11,23,4,20], h = 5
        - Try mid = 15 → hours = 8 (>5) → too slow → move right
        - Try mid = 23 → hours = 6 (>5) → too slow → move right
        - Try mid = 30 → hours = 5 (<=5) → valid → move left
        Answer = 30

        Time Complexity:
        ----------------
        - Binary search runs in O(log(maxPile)).
        - Each checkHours call scans all piles → O(n).
        - Total = O(n * log(maxPile)).

        Space Complexity:
        -----------------
        - O(1) extra space (only variables used).
        """

        # Binary search boundaries: speed between 1 and max pile size
        l, r = 1, max(piles)

        # Helper function: calculate hours needed at given speed
        def checkHours(hours, piles):
            total_hours = 0
            for x in piles:
                # Ceiling division: how many hours needed for pile 'x' at speed 'hours'
                if x % hours == 0:
                    total_hours += x // hours
                else:
                    total_hours += (x // hours) + 1
            return total_hours

        ans = 0
        # Binary search loop
        while l <= r:
            mid = (l + r) // 2  # candidate speed
            required_hours = checkHours(mid, piles)

            if required_hours <= h:
                # Valid speed → store answer and try smaller speed
                ans = mid
                r = mid - 1
            else:
                # Too slow → increase speed
                l = mid + 1

        return ans


# Example run
o = Solution()
a = o.minEatingSpeed([30, 11, 23, 4, 20], 5)
print(a)  # Output: 30
