# Approximation algorithm to find the minimum vertex cover

import random, time
from Graph import *

# Implementation of the approximation algorithm which takes the edges and minK as input.
def approximate_vertex(E,minK):
    C = []
    # creates a copy of the given edges to remove traveresed edges from.
    Edges_list = E.copy()
    # iterate until there are no more edges in the edges list.
    while len(Edges_list) > 0:
        # choose a random edge from the list
        choose_random_edge = random.randint(0, len(Edges_list)-1)
        c = Edges_list.pop(choose_random_edge)
        # add vertices incident on that edge to C
        C.append(c[0])
        C.append(c[1])
        # remove edges from Edges list where incident vertices already exist in C.
        for e in Edges_list:
            if e[0] in C or e[1] in C:
                Edges_list.remove(e)
    res = len(C)
    return [C,res < minK] 

# creates a input graph 
graphs,size = create_graphs()
# represent the random graph created as a Graph Object
graph_as_Graph = Graph(graphs, size)
# represents k (to check if a vertex cover exists that has a size less than the given integer )
# k is chosen to be a random integer between 1 and 10
minK = random.randint(1,10)
# save starting timestamp
start = time.time()
vertex_cover = approximate_vertex(graph_as_Graph.E,minK)
print("Approximation Algorithm")
if not vertex_cover[1]:
    print("Valid vertex cover with minimum k = " + str(minK)+" could not be found")
else:
    print("Valid vertex cover found, " + "\n" + "Minimum k = " + str(minK) + "\n" + "Vertex cover = " + str(vertex_cover[0]))

# save ending timestamp
end = time.time()
# return time required to run the program
print(f"Time taken for the program to run = {end-start} seconds")

    