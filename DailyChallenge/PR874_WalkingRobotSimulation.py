class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        """
        Simulates the movement of a robot on a 2D plane given a list of commands and obstacles.

        Problem Context (LeetCode: Walking Robot Simulation):
        - The robot starts at the origin (0,0), facing North.
        - Commands:
            * Positive integers (1 ≤ x ≤ 9): move forward x steps.
            * -1: turn right 90 degrees.
            * -2: turn left 90 degrees.
        - Obstacles: list of coordinates where the robot cannot move.
        - The robot must ignore an obstacle at (0,0) at the start, but cannot return to (0,0) later.
        - Goal: return the maximum Euclidean distance squared (x² + y²) from the origin
          that the robot reaches during its journey.

        Approach:
        1. Maintain current position (a, b) and direction (curr_dir).
        2. Use a helper function `changeDIR` to rotate left/right.
        3. Convert obstacles to a set for O(1) lookup.
        4. For each command:
            - If it's a turn, update direction.
            - If it's a move, step forward one unit at a time:
                * Stop if the next cell is an obstacle.
                * Update max_dist at each valid step.
        5. Return max_dist at the end.

        Time Complexity:
        - O(C + S) where C = number of commands, S = total steps moved.
        - Obstacle lookup is O(1) due to set usage.
        """

        def changeDIR(curr_dir, change_flag):
            """
            Rotate the robot's facing direction.
            - curr_dir: current direction ("N", "E", "S", "W")
            - change_flag: -1 (turn right), -2 (turn left)
            """
            DIR = ["N", "E", "S", "W"]   # clockwise order
            if change_flag == -1:        # turn right
                return DIR[(DIR.index(curr_dir) + 1) % 4]
            if change_flag == -2:        # turn left
                return DIR[(DIR.index(curr_dir) - 1 + 4) % 4]

        # Convert obstacles to set of tuples for O(1) lookup
        obs = set(map(tuple, obstacles))


        # Initial position and direction
        a, b = 0, 0
        curr_dir = "N"
        max_dist = 0  # track maximum distance squared

        # Process each command
        for i in commands:
            if i == -1 or i == -2:
                # Update direction if command is a turn
                curr_dir = changeDIR(curr_dir, i)
            else:
                # Move forward step by step
                if curr_dir == "N":
                    while i != 0:
                        b += 1
                        i -= 1
                        if (a, b) in obs:  # obstacle check
                            b -= 1
                            break
                        max_dist = max(max_dist, a*a + b*b)
                if curr_dir == "E":
                    while i != 0:
                        a += 1
                        i -= 1
                        if (a, b) in obs:
                            a -= 1
                            break
                        max_dist = max(max_dist, a*a + b*b)
                if curr_dir == "W":
                    while i != 0:
                        a -= 1
                        i -= 1
                        if (a, b) in obs:
                            a += 1
                            break
                        max_dist = max(max_dist, a*a + b*b)
                if curr_dir == "S":
                    while i != 0:
                        b -= 1
                        i -= 1
                        if (a, b) in obs:
                            b += 1
                            break
                        max_dist = max(max_dist, a*a + b*b)

        return max_dist
