class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        """
        Simulate robot collisions and return the healths of survivors.

        Approach (your stack logic, corrected):
        - Sort robots by position so we process them in movement order.
        - Use a stack to track robots moving right.
        - When a left-moving robot is encountered:
            * Collide with the stack top (right-moving robot).
            * Compare healths:
                - Lower health robot dies.
                - Higher health robot loses 1 health and continues.
                - Equal health → both die.
            * Repeat until no collision remains or the left robot dies.
        - Survivors are collected and returned in original index order.
        """
        # Bundle robots with their original index
        robots = sorted(zip(positions, healths, directions, range(len(positions))))
        stack = []

        for pos, health, dirr, idx in robots:
            if dirr == "R":
                # Right-moving robots always go on stack
                stack.append([pos, health, dirr, idx])
            else:  # dirr == "L"
                # Resolve collisions with right-moving robots in stack
                while stack and stack[-1][2] == "R" and health > 0:
                    if stack[-1][1] < health:
                        # Right robot dies
                        stack.pop()
                        health -= 1
                    elif stack[-1][1] > health:
                        # Left robot dies
                        stack[-1][1] -= 1
                        health = 0
                    else:
                        # Both die
                        stack.pop()
                        health = 0
                if health > 0:
                    stack.append([pos, health, dirr, idx])

        # Sort survivors back to original index order
        stack.sort(key=lambda x: x[3])
        return [robot[1] for robot in stack]
