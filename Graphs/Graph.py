class Graph:
    """
    Graph Data Structure
    
    A **graph** is a collection of **nodes (vertices)** connected by **edges**.
    Graphs are widely used to represent relationships such as:
    - Social networks (users connected by friendships)
    - Transportation systems (cities connected by roads)
    - Computer networks (devices connected by links)

    -----------------------------
    Key Definitions:
    -----------------------------
    • Vertex (Node): A fundamental unit of the graph.
    • Edge: A connection between two vertices.
    • Undirected Graph: Edges have no direction (A—B is same as B—A).
    • Directed Graph: Edges have direction (A → B).
    • Weighted Graph: Edges have weights (cost, distance, etc.).
    • Adjacency Matrix: A 2D matrix representation of connections.
    • Adjacency List: A dictionary mapping each node to its neighbors.
    • DFS (Depth First Search): Traversal that explores as far as possible
      along each branch before backtracking.

    -----------------------------
    Example Graph:
    -----------------------------
    Edges = [[0, 1], [0, 2], [1, 2], [1, 3]]

    ASCII Representation:
    
        (0) ----- (1)
         |      /  |
         |     /   |
         |    /    |
        (2)        (3)

    -----------------------------
    Adjacency Matrix:
    -----------------------------
    For nodes [0,1,2,3], matrix is:

        0 1 2 3
      0 0 1 1 0
      1 1 0 1 1
      2 1 1 0 0
      3 0 1 0 0

    -----------------------------
    Adjacency List:
    -----------------------------
    {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1],
        3: [1]
    }

    -----------------------------
    DFS Traversal (starting at 0):
    -----------------------------
    Visit order: [0, 1, 2, 3]
    """

    def __init__(self, edges):
        # Store edges (pairs of connected nodes)
        self.edges = edges
        # Initialize adjacency list as empty dictionary
        self.adjList = {}
        # Initialize adjacency matrix as empty list
        self.adjMatrix = []

    def createAdjacencyMatrix(self):
        """
        Create adjacency matrix representation of the graph.
        Matrix size = number of unique nodes.
        """
        M = []
        # Initialize matrix with zeros
        for i in range(len(self.edges)):
            M.append([0] * len(self.edges))
        # Fill matrix with 1s where edges exist
        for u, v in self.edges:
            M[u][v] = 1
            M[v][u] = 1  # undirected graph
            self.adjMatrix = M
        return M

    def createAdjacencyList(self):
        """
        Create adjacency list representation of the graph.
        Dictionary maps each node to its neighbors.
        """
        for u, v in self.edges:
            if u not in self.adjList:
                self.adjList[u] = []
            if v not in self.adjList:
                self.adjList[v] = []
            # Add neighbors (undirected graph)
            self.adjList[u].append(v)
            self.adjList[v].append(u)
        return self.adjList

    def DepthFirstSearchRecursive(self, start_node, seen):
        """
        Perform DFS recursively.
        - start_node: node to begin traversal
        - seen: set of visited nodes
        Returns: list of nodes visited in DFS order
        """
        arr = []
        seen.add(start_node)
        for nei_node in self.adjList[start_node]:
            if nei_node not in seen:
                seen.add(nei_node)
                arr.append(nei_node)
                # Recursive call to explore deeper
                arr.extend(self.DepthFirstSearchRecursive(nei_node, seen))
        return arr


# -----------------------------
# Example Usage
# -----------------------------
edges = [[0, 1], [0, 2], [1, 2], [1, 3]]
graph = Graph(edges)

# Create adjacency matrix
adjacency_matrix = graph.createAdjacencyMatrix()
print("Adjacency Matrix:")
print(adjacency_matrix)

# Create adjacency list
adjacency_list = graph.createAdjacencyList()
print("Adjacency List:")
print(adjacency_list)

# Perform DFS starting from node 0
seen = set()
seen.add(0)
dfs_result = [0]
dfs_result.extend(graph.DepthFirstSearchRecursive(0, seen))
print("DFS Traversal Result:")
print(dfs_result)
