# bfs.py -- implement breadth-first search in undirected graph

from collections import deque # use deque as queue, append and popleft

'''let G be the graph
   V be the num of vertex
   E be the num of edges
   adj be an array which contains the adjancency of each vertex'''

marked = [False for i in range(V)]
edgeTo = [-1 for i in range(V)]

def bfs(G, s):
    queue = deque()
    marked[s] = True
    queue.append(s)
    while queue:
        v = queue.popleft()
        for w in G.adj(v):
            edgeTo[w] = v
            marked[w] = True
            queue.append(w)

def hasPathTo(v):
    '''same as dfs'''
    pass

def pathTo(v):
    '''same as dfs'''
    pass
        