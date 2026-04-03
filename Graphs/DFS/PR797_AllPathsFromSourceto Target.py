from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        Problem:
        --------
        Given a directed acyclic graph (DAG), represented as an adjacency list,
        find all possible paths from the source node (0) to the target node (n-1).

        - graph[i] contains all nodes that node i can directly reach.
        - Return a list of all paths, where each path is a list of nodes.

        Approach:
        ---------
        - Use Depth-First Search (DFS) with backtracking.
        - Maintain a temporary list `temp` to store the current path.
        - When we reach the target node, append a COPY of `temp` to `result`.
        - Backtrack by removing the last node (`pop`) before exploring other paths.

        Key Mistake You Made:
        ---------------------
        - You originally wrote `result.append(temp)`.
        - This appends the same mutable list object, so all paths in `result`
          pointed to the same `temp` list and changed as DFS backtracked.
        - Correct fix: use `result.append(list(temp))` to store a snapshot copy.

        Complexity:
        -----------
        - Time: O(P) where P is the total number of paths (can be exponential).
        - Space: O(n) for recursion depth and temporary path storage.
        """

        def dfs(graph, source, target, result, temp):
            # Step 1: Add current node to path
            temp.append(source)

            # Step 2: If we reached target, save a copy of the path
            if source == target:
                result.append(list(temp))  # <-- snapshot copy

            # Step 3: Explore all neighbors
            for neighbor in graph[source]:
                dfs(graph, neighbor, target, result, temp)

            # Step 4: Backtrack (remove last node before returning)
            temp.pop()

        result = []
        dfs(graph, 0, len(graph) - 1, result, [])
        return result
