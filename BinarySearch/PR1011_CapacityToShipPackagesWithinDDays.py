class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        Problem:
        --------
        Find the minimum ship capacity required to deliver all packages
        within 'days'. Each package must be shipped in order, and the ship
        cannot exceed its capacity on any given day.

        Approach:
        ---------
        1. Use Binary Search on the answer (capacity).
           - Lower bound = max(weights)  (must fit the largest package).
           - Upper bound = sum(weights)  (capacity large enough to ship all in one day).
        2. For each mid capacity, simulate shipping using a helper function:
           - Traverse weights, accumulate until exceeding capacity.
           - If exceeded, start a new day.
           - Count how many days are needed.
        3. Adjust search space:
           - If days_needed <= days → capacity works, try smaller (r = mid).
           - Else → capacity too small, try larger (l = mid+1).
        4. Final answer is l (smallest valid capacity).

        ASCII Diagram of Search:
        ------------------------
        Capacity Range: [max(weights) ........ sum(weights)]
                        l                     r

        mid = (l+r)//2
        ┌───────────────┐
        │ checkDays(mid)│
        └───────────────┘
             ↓
        If days_needed <= days → shrink right (r = mid)
        Else → grow left (l = mid+1)

        Loop until l == r → l is the minimum capacity.

        Complexity:
        -----------
        - Time: O(n log(sum(weights)))
          (n = number of packages, log range of capacities)
        - Space: O(1) (only variables, no extra structures)
        """

        def checkDays(w, capacity):
            # Simulate shipping with given capacity
            total = 0
            d = 1  # start with day 1
            for x in w:
                total += x
                if total > capacity:
                    d += 1      # need another day
                    total = x   # start new day with current package
            return d

        # Binary search boundaries
        l, r = max(weights), sum(weights)

        while l < r:
            mid = (l + r) // 2
            if checkDays(weights, mid) <= days:
                # Capacity works → try smaller
                r = mid
            else:
                # Capacity too small → try larger
                l = mid + 1

        return l  # smallest valid capacity
