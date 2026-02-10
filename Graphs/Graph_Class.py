class Graph:
    """
    Graph Class Implementation
    
    A graph is a collection of nodes (vertices) connected by edges.
    This class represents a node in a graph.
    Key Concepts:
    - Node (Vertex): A fundamental unit of the graph.
    - Edge: A connection between two nodes.
    - Undirected Graph: Edges have no direction (A—B is same as B—A).
    - Directed Graph: Edges have direction (A → B).
    - Weighted Graph: Edges have weights (cost, distance, etc.).
    - Adjacency Matrix: A 2D matrix representation of connections.
    - Adjacency List: A dictionary mapping each node to its neighbors.
    - DFS (Depth First Search): Traversal that explores as far as possible
        along each branch before backtracking.
    Example Graph:
    Edges = [[0, 1], [0, 2], [1, 2], [1, 3]]
    ASCII Representation:
    
        (0) ----- (1)
         |      /  |
         |     /   |
         |    /    |
        (2)        (3)
    Adjacency Matrix:
    For nodes [0,1,2,3], matrix is:
        0 1 2 3
      0 0 1 1 0
      1 1 0 1 1
      2 1 1 0 0
      3 0 1 0 0
    Adjacency List:
    {
        0: [1, 2],  
        1: [0, 2, 3],
        2: [0, 1],
        3: [1]
    }
    DFS Traversal (starting at 0):
    Visit order: [0, 1, 2, 3]

    """
    def __init__(self , value):
        self.value = value
        self.neighbors = []

    def addNeighbor(self , neighbor):
        self.neighbors.append(neighbor)
    
    def __str__(self):
        return f"Graph Node: {self.value}, Neighbors: {[neighbor.value for neighbor in self.neighbors]}"
    

Node1 = Graph(0)
Node1.addNeighbor(Graph(1))
Node1.addNeighbor(Graph(2))
Node1.addNeighbor(Graph(3))
Node1.addNeighbor(Graph(4))

Node2 = Graph(1)
Node2.addNeighbor(Node1)



print(Node2)
   
