# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        Determine if a binary tree is height-balanced.

        A binary tree is considered balanced if:
        - The height difference between the left and right subtrees
          of every node is at most 1.
        - Both left and right subtrees are themselves balanced.

        Approach:
        ----------
        1. Define a helper function `height` that recursively computes
           the height of a subtree.
        2. For the current node:
           - Compute the height of left and right subtrees.
           - Check if their difference is <= 1.
           - Recursively ensure both subtrees are balanced.
        3. Return True if all conditions hold, otherwise False.

        Time Complexity:
        - O(n^2) in worst case (because height is recomputed for each node).
        - Can be optimized to O(n) by combining balance check and height
          computation in one pass.

        Example Diagram:
        ----------------
                1
               / \
              2   3
             / \
            4   5

        Heights:
        - Node 4 → height = 1
        - Node 5 → height = 1
        - Node 2 → height = 2
        - Node 3 → height = 1
        - Node 1 → height = 3
        Balance check:
        - abs(height(2) - height(3)) = abs(2 - 1) = 1 → Balanced ✅

        Returns:
        --------
        True if the tree is balanced, False otherwise.
        """

        if root is None:
            return True

        def height(root):
            # Base case: empty subtree has height 0
            if not root:
                return 0
            # Height = 1 + max(left subtree height, right subtree height)
            return 1 + max(height(root.left), height(root.right))

        # Compute heights of left and right subtrees
        left_height = height(root.left)
        right_height = height(root.right)

        # Check balance condition at current node AND recurse into subtrees
        return abs(left_height - right_height) <= 1 and \
               self.isBalanced(root.left) and \
               self.isBalanced(root.right)
