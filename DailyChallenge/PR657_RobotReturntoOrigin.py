class Solution:
    def judgeCircle(self, moves: str) -> bool:
        """
        Determine whether a robot returns to its original position after executing a sequence of moves.

        Problem Context:
        ----------------
        - The robot starts at the origin point (0, 0) on a 2D plane.
        - It can move in four directions:
            'R' → move right (increase x-coordinate by 1)
            'L' → move left (decrease x-coordinate by 1)
            'U' → move up (increase y-coordinate by 1)
            'D' → move down (decrease y-coordinate by 1)
        - After executing all moves in the given string, we check if the robot is back at the origin.

        Parameters:
        -----------
        moves : str
            A string consisting of characters 'R', 'L', 'U', 'D' representing the robot's moves.

        Returns:
        --------
        bool
            True if the robot returns to the origin (0, 0), False otherwise.

        Example:
        --------
        >>> Solution().judgeCircle("UD")
        True   # Up then Down cancels out, robot returns to origin

        >>> Solution().judgeCircle("LL")
        False  # Two left moves leave robot at (-2, 0), not at origin
        """

        # Initialize coordinates for the robot's position.
        # x → horizontal axis, y → vertical axis
        x, y = 0, 0

        # Iterate through each move in the input string
        for i in moves:
            if i == "R":
                x += 1   # Move right → increase x
            elif i == "L":
                x -= 1   # Move left → decrease x
            elif i == "U":
                y += 1   # Move up → increase y
            else:
                y -= 1   # Move down → decrease y

        # Robot returns to origin if both x and y are zero
        return (x == 0 and y == 0)
