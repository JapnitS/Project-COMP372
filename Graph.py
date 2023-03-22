# Graph class to represent graphs objects as 2-D matrices where 
# graph[i][j] = 1 represents a valid edge between vertex i and vertex j

import random

class Graph:
    def __init__(self, graph, size) -> None:
        self.graph = graph
        self.size = size
        self.E = self.get_edges(graph,size)
        self.V = range(size)

    def get_edges(self, graph, size):
        edges = []
        for i in range(size):
            for j in range(i, size):
                if graph[i][j] == 1:
                    edges.append((i,j))
        return edges

# method which creates a random graph (as a 2D matrix) of a random size ranging from 3 to 10.
def create_graphs():
    
    size = random.randint(3, 10)
    # initializes the matrix with 0s and 1s randomly, 1 represents a valid edge.
    graph = [[random.randint(0,1) for i in range(size)] for j in range(size)]
    # makes sure a vertex does not contain an edge to itself.
    for i in range(size):
        graph[i][i] = 0
    return [graph, size]

                    
