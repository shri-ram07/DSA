from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Return a possible order in which to complete all courses given prerequisites.

        This uses **Kahn's Algorithm** (BFS-based topological sort).

        Parameters
        ----------
        numCourses : int
            Total number of courses labeled from 0 to numCourses-1.
        prerequisites : List[List[int]]
            Each pair [u, v] means course `u` depends on course `v` 
            (i.e., you must take `v` before `u`).

        Returns
        -------
        List[int]
            A list of courses in a valid order that satisfies prerequisites.
            If no valid ordering exists (due to cycles), return an empty list.

        Algorithm Explanation
        ---------------------
        1. Build an adjacency list `ad` where each key is a course, and values are
           the list of courses that depend on it (edges v → u).
        2. Maintain an `inDegree` dictionary that counts how many prerequisites
           each course has (number of incoming edges).
        3. Initialize a queue with all courses having `inDegree == 0` (no prerequisites).
        4. Repeatedly pop from the queue:
            - Add the course to the topological order.
            - For each neighbor (dependent course), decrement its in-degree.
            - If a neighbor’s in-degree becomes 0, add it to the queue.
        5. If we processed all courses, return the order. Otherwise, return [].

        Why increment inDegree[u]?
        ---------------------------
        For each prerequisite pair [u, v]:
        - Edge is v → u (v must be taken before u).
        - Therefore, `u` has one more incoming edge (dependency).
        - So we increment `inDegree[u]`.

        Example
        -------
        numCourses = 4
        prerequisites = [[1,0],[2,0],[3,1],[3,2]]

        Graph:
            0 → 1
            0 → 2
            1 → 3
            2 → 3

        Valid order: [0,1,2,3] or [0,2,1,3]
        """

        # Step 1: Build adjacency list and in-degree map
        ad = {i: [] for i in range(numCourses)}   # adjacency list
        inDegree = {x: 0 for x in range(numCourses)}  # in-degree counts

        for u, v in prerequisites:
            ad[v].append(u)       # v → u (u depends on v)
            inDegree[u] += 1      # increment in-degree of u

        # Step 2: Initialize queue with nodes having in-degree 0
        queue = []
        for i in inDegree:
            if inDegree[i] == 0:
                queue.append(i)

        topologicalOrder = []

        # Step 3: Process queue
        while queue:
            a = queue.pop(0)          # dequeue
            topologicalOrder.append(a) # add to result

            # Reduce in-degree of neighbors
            for j in ad[a]:
                inDegree[j] -= 1
                if inDegree[j] == 0:
                    queue.append(j)

        # Step 4: Check if all courses are processed
        if len(topologicalOrder) == numCourses:
            return topologicalOrder
        else:
            return []
