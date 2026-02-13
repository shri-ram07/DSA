# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        """
        Clone an undirected graph using BFS (Breadth-First Search).

        -------------------------------
        Problem:
        Given a reference to a node in a connected undirected graph,
        return a deep copy (clone) of the graph.

        Each node contains:
            - val: unique integer value
            - neighbors: list of adjacent nodes

        -------------------------------
        Approach:
        1. Use a HashMap (dictionary) to store mapping:
               { original_node : cloned_node }
           This ensures we don’t re-clone nodes and can reuse already cloned ones.

        2. BFS traversal:
            - Start with the given node.
            - For each node, visit all its neighbors.
            - If a neighbor hasn’t been cloned yet:
                * Create a new clone.
                * Add it to the HashMap.
                * Enqueue the neighbor for later processing.
            - Append the cloned neighbor to the current cloned node’s neighbors list.

        -------------------------------
        Diagram Example:

            Original Graph:
                1
               / \
              2   3
               \ /
                4

            Step-by-step cloning:
            - Start at node 1 → clone Node(1)
            - Visit neighbors (2,3):
                * Clone Node(2), enqueue
                * Clone Node(3), enqueue
            - Append cloned neighbors to Node(1)’s neighbors
            - Continue BFS for Node(2), Node(3), etc.
            - Eventually Node(4) is cloned and linked properly.

            Result:
            A completely new graph with same structure but independent nodes.

        -------------------------------
        Why BFS?
        - BFS ensures level-by-level traversal.
        - DFS works too, but BFS avoids deep recursion and stack overflow in large graphs.

        -------------------------------
        Time Complexity:
            O(V + E) → V = number of nodes, E = number of edges
        Space Complexity:
            O(V) for HashMap + O(V) for queue

        -------------------------------
        Returns:
            Cloned node corresponding to the input node.
        """

        if not node:
            return None

        # Dictionary to map original nodes to their clones
        HashMap = {node: Node(node.val)}

        # Queue for BFS traversal
        queue = [node]

        while queue:
            curr = queue.pop(0)  # Dequeue
            cloned_curr = HashMap[curr]

            # Traverse neighbors
            for neighbor in curr.neighbors:
                if neighbor not in HashMap:
                    # Clone neighbor if not already cloned
                    HashMap[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)  # Enqueue for BFS
                # Append cloned neighbor to current cloned node
                cloned_curr.neighbors.append(HashMap[neighbor])

        return HashMap[node]
