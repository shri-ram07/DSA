# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inOrder(root, arr):
    """
    Perform an inorder traversal of the binary tree.

    Inorder traversal rule: LEFT → ROOT → RIGHT

    Example:
        Tree:       2
                  /   \
                 1     3

        Inorder result: [1, 2, 3]

    Parameters:
    root (TreeNode): Current node of the tree.
    arr (list): Array to store traversal result.

    Returns:
    list: Sorted list of node values.
    """
    if root:
        inOrder(root.left, arr)      # Visit left subtree
        arr.append(root.val)         # Visit root
        inOrder(root.right, arr)     # Visit right subtree
    return arr


def constructTreeNode(l, r, vec):
    """
    Construct a balanced BST from a sorted array.

    Logic:
    - Pick the middle element as the root (to ensure balance).
    - Recursively build left subtree from left half of array.
    - Recursively build right subtree from right half of array.

    Example:
        Sorted array: [1, 2, 3, 4]

        Step 1: mid = 2 → root = 2
        Step 2: Left subtree from [1]
        Step 3: Right subtree from [3, 4]

        Resulting Balanced Tree:
                2
              /   \
             1     3
                    \
                     4

    Parameters:
    l (int): Left index of array segment.
    r (int): Right index of array segment.
    vec (list): Sorted array of node values.

    Returns:
    TreeNode: Root of constructed balanced BST.
    """
    if l > r:
        return None
    mid = (l + r) // 2
    Node = TreeNode(vec[mid])  # Middle element becomes root
    Node.left = constructTreeNode(l, mid - 1, vec)   # Build left subtree
    Node.right = constructTreeNode(mid + 1, r, vec)  # Build right subtree
    return Node


class Solution(object):
    def balanceBST(self, root):
        """
        Balance a Binary Search Tree (BST).

        ------------------------------------------------------------
        STEP-BY-STEP LOGIC:
        1. Perform inorder traversal of the BST.
           - This gives a sorted array of node values.
        2. Use the sorted array to construct a balanced BST.
           - Always choose the middle element as root.
           - Recursively build left and right subtrees.

        ------------------------------------------------------------
        WHY THIS WORKS:
        - Inorder traversal of a BST always produces sorted values.
        - Choosing the middle element ensures minimal height and balance.

        ------------------------------------------------------------
        DIAGRAM EXAMPLE:

        Input Tree (Unbalanced):
                1
                 \
                  2
                   \
                    3
                     \
                      4

        Step 1: Inorder Traversal → [1, 2, 3, 4]

        Step 2: Construct Balanced BST:
                2
              /   \
             1     3
                    \
                     4

        ------------------------------------------------------------
        COMPLEXITY:
        - Time: O(n) (inorder + construction)
        - Space: O(n) (array storage + recursion stack)

        Parameters:
        root (TreeNode): Root of the input BST.

        Returns:
        TreeNode: Root of the balanced BST.
        """
        arr = []
        arr = inOrder(root, arr)  # Step 1: Get sorted array
        l, r = 0, len(arr) - 1
        return constructTreeNode(l, r, arr)  # Step 2: Build balanced BST
