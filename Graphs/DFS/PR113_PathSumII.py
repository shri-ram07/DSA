class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        Path Sum II (LeetCode Problem):
        --------------------------------
        Given a binary tree and a target sum, return all root-to-leaf paths
        where the sum of node values equals targetSum.

        Key DFS Intuition:
        - DFS explores one path fully before backtracking.
        - Maintain a running path (list of nodes) and a running sum.
        - At each node:
            1. Choose → add node to path and update sum.
            2. Check → if leaf and sum == target, record the path.
            3. Explore → recurse into left and right children.
            4. Backtrack → remove node from path before returning.

        Important Notes:
        - `path` is mutable → must backtrack with `pop()`.
        - `curr_sum` is immutable (int) → no manual undo needed, recursion restores it.
        - Always copy the path (`list(path)`) when saving, because lists are shared.
        """

        def dfs(node, path, curr_sum):
            if not node:
                return  # base case: null node, stop recursion

            # 1. Choose: include current node in path and sum
            path.append(node.val)
            curr_sum += node.val

            # 2. Check: if leaf node and sum matches target
            if not node.left and not node.right and curr_sum == targetSum:
                result.append(list(path))  # copy current path

            # 3. Explore: recurse into children
            dfs(node.left, path, curr_sum)
            dfs(node.right, path, curr_sum)

            # 4. Backtrack: undo the choice (remove last node)
            path.pop()

        result = []
        dfs(root, [], 0)
        return result
