# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        """
        Problem:
        --------
        Given a binary tree where each node contains a binary digit (0 or 1),
        compute the sum of all root-to-leaf paths interpreted as binary numbers.

        Approach (Recursive DFS):
        -------------------------
        - Use Depth First Search (DFS) recursion to traverse the tree.
        - At each node, carry forward the "binary number" built so far.
          This is done by shifting the current value left (multiply by 2)
          and adding the node's value.
        - When a leaf node is reached (no left or right child),
          return the final binary number for that path.
        - Sum up results from left and right subtrees.

        Key Idea:
        ---------
        - Binary numbers grow by "shift left + add bit".
          Example: path 1 → 0 → 1
          Step 1: 1
          Step 2: (1 << 1) + 0 = 2
          Step 3: (2 << 1) + 1 = 5
          Final = 5 (binary 101)

        Complexity:
        -----------
        - Time Complexity: O(N), where N = number of nodes.
          Each node is visited exactly once.
        - Space Complexity: O(H), where H = height of the tree.
          This is the recursion stack depth (worst case O(N) for skewed tree,
          best case O(log N) for balanced tree).
        """

        def recur(root, value):
            # Base case: if node is None, return 0 (no contribution)
            if root is None:
                return 0

            # Update the path value:
            # Multiply by 2 (shift left) and add current node's bit
            value = (2 * value) + root.val

            # If this is a leaf node, return the final path value
            if root.left is None and root.right is None:
                return value

            # Otherwise, recurse into left and right children
            # and sum their contributions
            return recur(root.left, value) + recur(root.right, value)

        # Start recursion from root with initial value = 0
        return recur(root, 0)
