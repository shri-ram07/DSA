class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Perform a level order traversal (Breadth-First Search) of a binary tree.

        Problem Context:
        ----------------
        - Given the root of a binary tree, return its level order traversal.
        - Level order means visiting nodes level by level from left to right.

        Approach:
        ---------
        1. Use a queue to process nodes in FIFO order.
        2. For each level:
           - Determine the number of nodes currently in the queue (this is the level size).
           - Pop nodes one by one, record their values, and enqueue their children.
           - Append the collected values for the level to the result list.
        3. Continue until the queue is empty.

        Time Complexity: O(N)  -> Each node is visited once.
        Space Complexity: O(N) -> Queue can hold up to N nodes in worst case.

        Diagram Example:
        ----------------
                3
               / \
              9   20
                 /  \
                15   7

        Step-by-step traversal:
        - Level 1: [3]
        - Level 2: [9, 20]
        - Level 3: [15, 7]

        Output:
        [[3], [9, 20], [15, 7]]
        """

        if not root:
            return []

        queue = [root]   # Initialize queue with root node
        ordered = []     # Final result list

        while queue:
            arr = []     # Stores values for current level

            # Process all nodes in the current level
            for i in range(len(queue)):
                a = queue.pop(0)       # Pop first node in queue

                if a:                  # Ensure node is not None
                    arr.append(a.val)  # Append node value to current level

                    # Enqueue left and right children for next level
                    if a.left:
                        queue.append(a.left)
                    if a.right:
                        queue.append(a.right)

            ordered.append(arr)        # Add current level values to result

        return ordered
