class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        Find the minimum depth of a binary tree.

        Minimum depth means:
        - The shortest distance from the root node down to the nearest leaf node.
        - A leaf node is a node with no left or right child.

        Approach:
        - Use Breadth-First Search (BFS) with a queue.
        - Start from the root at depth = 1.
        - Traverse level by level:
            * For each node, check if it is a leaf.
            * If yes, return the current depth immediately (because BFS guarantees
              this is the shortest path).
            * Otherwise, add its children to the queue for the next level.
        - Continue until a leaf is found.

        Why BFS works best here:
        - BFS explores level by level.
        - The first leaf encountered is guaranteed to be at the minimum depth.

        Example:
            Input Tree:
                    1
                   / \
                  2   3
                 /
                4

            Output:
                2   (because node 3 is the nearest leaf)

        Time Complexity:
            O(N) — Each node is visited once.
        Space Complexity:
            O(N) — Queue storage in the worst case.
        """
        if not root:
            return 0

        queue = [root]   # Start BFS with root node
        dep = 1          # Depth counter begins at 1 (root level)

        while queue:
            for i in range(len(queue)):
                a = queue.pop(0)  # FIFO: process nodes in order

                # If this node is a leaf, we found the minimum depth
                if not a.left and not a.right:
                    return dep

                # Otherwise, enqueue children for next level
                if a.left:
                    queue.append(a.left)
                if a.right:
                    queue.append(a.right)

            # After finishing one level, increase depth
            dep += 1

        return dep
