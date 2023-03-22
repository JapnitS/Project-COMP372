# brute force algorithm to find a vertex cover less than k

import itertools, time, random
from Graph import *



# method finds all possible subgraph combinations that can be created by G.
def all_subgraph_combinations(G, k):
    r = range(0, G.size)
    combs = list(itertools.combinations(r, k))
    return combs

# method to check if a given combination (subgraph of G) is able to reach all incident edges.
# calculates incident edges reachable by the current combination and checks if it equals the number of all edges in G
def is_vertex(G, comb):
    incident_edge = 0
    
    for e in G.E:
        if e[0] in comb or e[1] in comb:
            incident_edge += 1
    if incident_edge == len(G.E):
        return True
    else: return False

    
def find_minimum_vertex(G,minK):
  for k in range (1, G.size):
      combinations = all_subgraph_combinations(G, k)
      for c in combinations:
          # if we find a valid combination we check if the length of the combination is less than k 
          # if it is < k we return True otherwise False
          if is_vertex(G, c) and len(c) < minK:
              return [c, True]
  return [None, False]


# creates a input graph 
graphs,size = create_graphs()
# represent the random graph created as a Graph Object
graph_as_Graph = Graph(graphs, size)
# represents k (to check if a vertex cover exists that has a size less than the given integer )
# k is chosen to be a random integer between 1 and 10
minK = random.randint(1,10)
# save starting timestamp
start = time.time()
res = find_minimum_vertex(graph_as_Graph,minK)
print("Brute Force Algorithm")
if not res[1]:
    print("Valid vertex cover with minimum k = " + str(minK)+" could not be found")
else:
    print("Valid vertex cover found, " + "\n" + "Minimum k = " + str(minK) + "\n" + "Vertex cover = " + (str(res[0])))

# save ending timestamp
end = time.time()
# return time required to run the program
print(f"Time taken for the program to run = {end-start} seconds")