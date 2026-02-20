class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        Determines if all courses can be finished given prerequisites using Kahn's Algorithm.

        Kahn's Algorithm (Topological Sort via BFS):
        ------------------------------------------------
        - Build an adjacency list to represent course dependencies.
        - Compute in-degree (number of prerequisites) for each course.
        - Initialize a queue with all courses having in-degree = 0 (no prerequisites).
        - Repeatedly remove courses from the queue:
            * Add them to the ordering (or count them as processed).
            * Reduce in-degree of their dependent courses.
            * If any dependent course’s in-degree becomes 0, add it to the queue.
        - If all courses are processed, return True (possible to finish).
        - If some remain unprocessed, return False (cycle exists → impossible).

        Args:
            numCourses (int): Total number of courses.
            prerequisites (List[List[int]]): List of prerequisite pairs [course, prerequisite].

        Returns:
            bool: True if all courses can be finished, False otherwise.
        """

        # Step 1: Initialize in-degree for all courses
        indegree = {i: 0 for i in range(numCourses)}

        # Step 2: Build adjacency list
        ad_li = {}
        for u, v in prerequisites:
            if v not in ad_li:
                ad_li[v] = []
            ad_li[v].append(u)   # v → u (u depends on v)
            indegree[u] += 1     # increase in-degree of course u

        # Step 3: Collect all courses with no prerequisites
        queue = [i for i in indegree if indegree[i] == 0]

        # Step 4: Process queue using BFS
        count = 0
        while queue:
            course = queue.pop(0)
            count += 1
            if course in ad_li:
                for neighbor in ad_li[course]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)

        # Step 5: Check if all courses were processed
        return count == numCourses
