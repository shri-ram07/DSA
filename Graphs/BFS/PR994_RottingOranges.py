class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Rotting Oranges — Multi-Source BFS (manual queue version)
        ---------------------------------------------------------

        Problem summary
        ---------------
        You are given a grid where:
            0 = empty cell
            1 = fresh orange
            2 = rotten orange

        Every minute, any fresh orange adjacent (4-directionally) to a rotten one
        becomes rotten.

        Return the minimum minutes required until no fresh oranges remain.
        If impossible, return -1.

        ---------------------------------------------------------
        WHY MULTI-SOURCE BFS?
        ---------------------------------------------------------
        All rotten oranges spread infection *simultaneously*.
        That means time should advance in layers:

        minute 0 → initial rotten oranges
        minute 1 → newly infected from ALL of them
        minute 2 → next wave
        ...

        So we must start BFS from ALL rotten oranges at once.

        ---------------------------------------------------------
        ASCII VISUALIZATION
        ---------------------------------------------------------

        Example grid:

            2 1 1
            1 1 0
            0 1 1

        minute = 0
        queue = all rotten cells
        queue = [(0,0)]

            [2][1][1]
            [1][1][0]
            [0][1][1]

        ---------------------------------------------------------
        minute = 1
        rotten spreads from (0,0)

        new_queue = [(0,1), (1,0)]

            [2][2][1]
            [2][1][0]
            [0][1][1]

        ---------------------------------------------------------
        minute = 2

        new_queue = [(0,2), (1,1)]

            [2][2][2]
            [2][2][0]
            [0][1][1]

        ---------------------------------------------------------
        minute = 3

        new_queue = [(2,1)]

            [2][2][2]
            [2][2][0]
            [0][2][1]

        ---------------------------------------------------------
        minute = 4

        new_queue = [(2,2)]

            [2][2][2]
            [2][2][0]
            [0][2][2]

        All fresh gone → answer = 4

        ---------------------------------------------------------
        CORE IDEA
        ---------------------------------------------------------
        We perform BFS in LEVELS.

        queue      → all rotten oranges at current minute
        new_queue  → oranges that will rot next minute

        After processing one level:
            minutes += 1

        ---------------------------------------------------------
        IMPORTANT EDGE CASES
        ---------------------------------------------------------
        1. No fresh oranges → return 0
        2. Fresh exist but cannot be reached → return -1
        3. Empty grid → return -1

        ---------------------------------------------------------
        TIME COMPLEXITY
        ---------------------------------------------------------
        O(rows * cols)
        Each cell visited at most once.

        SPACE COMPLEXITY
        ---------------------------------------------------------
        O(rows * cols) for queue in worst case.

        ---------------------------------------------------------
        MANUAL QUEUE STYLE
        ---------------------------------------------------------
        We intentionally use:
            queue = []
            new_queue = []

        instead of deque,
        to keep BFS layer logic very explicit and interview-friendly.
        """

        if not grid:
            return -1

        rows, cols = len(grid), len(grid[0])

        # Manual queue storing all currently rotten oranges
        queue = []

        # Count fresh oranges
        fresh = 0

        # -------------------------------------------------
        # STEP 1: Initialize queue with ALL rotten oranges
        # -------------------------------------------------
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        # If no fresh oranges exist
        if fresh == 0:
            return 0

        minutes = 0

        # -------------------------------------------------
        # STEP 2: BFS level traversal
        # Each loop = 1 minute
        # -------------------------------------------------
        while queue and fresh > 0:
            new_queue = []

            # Process all rotten oranges of current minute
            for x, y in queue:

                # 4-direction neighbors
                neighbors = [
                    (x, y - 1),
                    (x, y + 1),
                    (x - 1, y),
                    (x + 1, y),
                ]

                for nx, ny in neighbors:
                    # Check bounds and fresh orange
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2   # Rot it
                        fresh -= 1
                        new_queue.append((nx, ny))

            # If we rotted at least one orange this minute
            if new_queue:
                minutes += 1

            queue = new_queue

        # -------------------------------------------------
        # STEP 3: Check if any fresh remain
        # -------------------------------------------------
        if fresh > 0:
            return -1

        return minutes
