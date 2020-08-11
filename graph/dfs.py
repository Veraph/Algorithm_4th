# dfs.py -- implement depth-first-search in undirected graphs

from collections import deque # use deque as stack, append and pop function

'''let G be the graph
   V be the num of vertex
   E be the num of edges
   adj be an array which contains the adjancency of each vertex'''

marked = [False for i in range(V)]
edgeTo = [-1 for i in range(V)]


def dfs(G, v):
    '''visit and mark v and its adjancencys vertex, and update edgeto'''
    marked[v] = True
    for i in G.adj(v):
        if !marked[i]:
            edgeTo[i] = v
            dfs(G, i)

def hasPathTo(G, v):
    '''return true if has path to v'''
    return marked[v]

def pathTo(G, v):
    '''return the path to v'''
    if !hasPathTo[v]:
        return None
    path = deque()
    while v != root:
        path.append(v)
        v = edgeTo[v]
    path.append(root)
    return path

#-------------------------Dfs to find connected components in a graph------------------------------------#
'''do dfs through all vertices by using adjancency
   When one round finish, increment count to move to
   another component'''

def cc(G):
    count = 0
    marked = [False for i in range(V)]
    id = [0 for i in range(V)]
    for s in range(0, V):
        is !marked[s]:
        dfs(G, s)
        count += 1

def dfs(G, v):
    marked[v] = True
    id[v] = count
    for w in G.adj(v):
        if !marked[w]:
            dfs(G, w)