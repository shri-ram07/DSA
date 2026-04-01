class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Perform a zigzag (spiral) level order traversal of a binary tree.

        A zigzag traversal alternates the direction of node values at each level:
        - Level 0 (root level): left → right
        - Level 1: right → left
        - Level 2: left → right
        - and so on...

        Args:
            root (TreeNode | None): The root node of the binary tree.

        Returns:
            List[List[int]]: A list of lists, where each inner list contains the
            node values at that level, ordered according to zigzag traversal.

        Example:
            Input Tree:
                    1
                   / \
                  2   3
                 / \   \
                4   5   6

            Output:
                [[1], [3, 2], [4, 5, 6]]

        Approach:
            - Use a queue to perform standard BFS (level order traversal).
            - At each level:
                * Collect all node values in an array.
                * Enqueue children (left → right) for the next level.
                * Reverse the array if the level index is odd.
            - Append the processed array to the result list.
            - Continue until the queue is empty.

        Time Complexity:
            O(N) — Each node is visited once.
        Space Complexity:
            O(N) — Queue and result storage.
        """
        if not root:
            return []

        queue = [root]   # BFS queue initialized with root
        result = []      # Final zigzag traversal result
        level = 0        # Track current level index

        while queue:
            arr = []     # Collect values for this level
            for i in range(len(queue)):
                a = queue.pop(0)  # FIFO: process nodes in order
                arr.append(a.val)

                # Always enqueue children left → right
                if a.left:
                    queue.append(a.left)
                if a.right:
                    queue.append(a.right)

            # Reverse values at odd levels to achieve zigzag
            if level % 2 == 1:
                arr.reverse()

            result.append(arr)
            level += 1   # Move to next level

        return result
