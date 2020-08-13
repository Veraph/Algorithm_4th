# Undirected-Graph notes
## Depth-first search(DFS)

## Breadth-first search(BFS)

# Directed-Graph notes

# Minimum Spanning Tree
Given an undirected edge-weight graph, find an MST
## Assumptions needed
1. graph is connected (if graph is not connected, we can compute the minimum spanning forest)
2. the edge weights are not necessarily distances
3. edge weights may be zero or negative
4. edge weights are all different(with arbitrary but distinct)  
### Cut property
The shortest crossing edge for every cut must be in the MST(Greedy MST algorithm)

## Prim's Algorithm

## Kruskal's algorithm(space E, time ElogE)
1. continues add the minimum edge(consider a priority queue to store) which will not create a cycle in the present tree
2. generally slower than prim algorithm  

Attention! Prim's amd Kruskal's algorithms do not work for directed graphs.

# Shortest Paths
Find the lowest-cost way to get from one vertex to another.
## Shortest Path Tree
A subgraph contain source s and all vertices reachable from s.
### Edge Relaxation
relax an edge v -> w means: test whether the best known way from s to w is to go from s to v and then from v to w
### Vertex Relaxation
### oprimality condition
### Dijkstra's algorithm
1. solve the single sourde shortest-paths problem in edge-weighted digraphs with nonnegative weights.
2. adds next the non-tree vertex that is closest to the source