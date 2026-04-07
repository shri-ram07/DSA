# from typing import List

# class Robot:
#     """
#     Simulates a robot moving along the boundary of a rectangular grid.

#     Grid size: width x height
#     - Robot starts at (0, 0)
#     - Initial direction: East
#     - Movement is restricted to the perimeter (edges only)

#     Key Optimization:
#     -----------------
#     Instead of simulating each step individually (O(num)),
#     we reduce steps using modulo with the perimeter length.

#     Perimeter (cycle length):
#         2 * (width - 1 + height - 1)

#     Important Edge Case:
#     --------------------
#     If num % perimeter == 0:
#         → Robot completes a full cycle
#         → Direction MUST change (important for correctness)

#     Directions follow clockwise order:
#         East → North → West → South → East ...
#     """

#     def __init__(self, width: int, height: int):
#         """
#         Initialize robot state.

#         We reduce width and height by 1 because:
#         - Coordinates go from 0 to width-1 and 0 to height-1
#         - This makes boundary calculations easier

#         Example:
#             width = 6 → valid x: 0 to 5 → max index = 5
#         """
#         self.width = width - 1
#         self.height = height - 1

#         # Current position
#         self.x, self.y = 0, 0

#         # Initial direction
#         self.curr_dir = "East"

#         # Total steps to complete one full boundary loop
#         self.perimeter = 2 * (self.width + self.height)

#     def step(self, num: int) -> None:
#         """
#         Move the robot 'num' steps along the boundary.

#         Optimization:
#         -------------
#         Reduce steps using modulo:
#             num = num % perimeter

#         Special case:
#             If num == 0 → treat as full cycle
#         """

#         # If grid is 1x1 → no movement possible
#         if self.perimeter == 0:
#             return

#         # Reduce unnecessary full cycles
#         num %= self.perimeter

#         # IMPORTANT:
#         # If num becomes 0, it means a full cycle is completed.
#         # We must still simulate one full loop to update direction correctly.
#         if num == 0:
#             num = self.perimeter

#         # Process movement in chunks (edge by edge)
#         while num > 0:

#             # ---------------- EAST ----------------
#             if self.curr_dir == "East":

#                 # If already at right boundary → turn North
#                 if self.x == self.width:
#                     self.curr_dir = "North"
#                     continue  # re-evaluate with new direction

#                 # Move as much as possible in current direction
#                 move = min(num, self.width - self.x)
#                 self.x += move
#                 num -= move

#             # ---------------- NORTH ----------------
#             elif self.curr_dir == "North":

#                 # If already at top boundary → turn West
#                 if self.y == self.height:
#                     self.curr_dir = "West"
#                     continue

#                 move = min(num, self.height - self.y)
#                 self.y += move
#                 num -= move

#             # ---------------- WEST ----------------
#             elif self.curr_dir == "West":

#                 # If already at left boundary → turn South
#                 if self.x == 0:
#                     self.curr_dir = "South"
#                     continue

#                 move = min(num, self.x)
#                 self.x -= move
#                 num -= move

#             # ---------------- SOUTH ----------------
#             elif self.curr_dir == "South":

#                 # If already at bottom boundary → turn East
#                 if self.y == 0:
#                     self.curr_dir = "East"
#                     continue

#                 move = min(num, self.y)
#                 self.y -= move
#                 num -= move

#     def getPos(self) -> List[int]:
#         """
#         Returns current position of robot.

#         Output:
#             [x, y]
#         """
#         return [self.x, self.y]

#     def getDir(self) -> str:
#         """
#         Returns current direction robot is facing.

#         One of:
#             "East", "North", "West", "South"
#         """
#         return self.curr_dir
class Robot:

    TO_DIR = {
        0: "East",
        1: "North",
        2: "West",
        3: "South",
    }

    def __init__(self, width: int, height: int):
        self.moved = False
        self.idx = 0
        self.pos = list()
        self.dirs = list()

        pos_, dirs_ = self.pos, self.dirs

        for i in range(width):
            pos_.append((i, 0))
            dirs_.append(0)
        for i in range(1, height):
            pos_.append((width - 1, i))
            dirs_.append(1)
        for i in range(width - 2, -1, -1):
            pos_.append((i, height - 1))
            dirs_.append(2)
        for i in range(height - 2, 0, -1):
            pos_.append((0, i))
            dirs_.append(3)

        dirs_[0] = 3

    def step(self, num: int) -> None:
        self.moved = True
        self.idx = (self.idx + num) % len(self.pos)

    def getPos(self) -> List[int]:
        return list(self.pos[self.idx])

    def getDir(self) -> str:
        if not self.moved:
            return "East"
        return Robot.TO_DIR[self.dirs[self.idx]]