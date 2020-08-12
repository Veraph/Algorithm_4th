# prim.py -- Algorithm to find the Miniumum spinning tree in the graph
'''G stands for Graph project, and assume it is a connected graph
   V stands for num of vertex
   E stands for num of edges'''

#------------------------------The lazy edition-----------------------------------
from queue import PriorityQueue
def lazy_prim(G):
    marked = [False for i in range(V)] # store the vist status of vertex
    mst_pq = PriorityQueue() # store the edges used in the mst
    ce_pq = PriorityQueue() # store the crossing edges used in the process

    visit(G, 0)
    while ce_pq:
        e = ce_pq.get()
        v = e.either()
        w = e.other(v)
        if marked[v] and marked[w]:
            continue
        mst_pq.put(e)
        if !marked[v]:
            visit(G, v)
        if !marked[w]:
            visit(G, w)

def visit(G, v):
    marked[v] = True
    for e in G.adj(v):
        if !marked[e.other(v)]:
            ce_pq.put(e)

#-------------------------------The eager version---------------------------------
def eager_prim(G):
    edgeTo = [-1 for i in range(V)]
    distTo = [0 for i in range(V)]
    marked = [False for in range(V)]
    pq = PriorityQueue()
    for v in range(0, V):
        distTo[v] = Infinity

    distTo[0] = 0.0
    pq.put(0, 0.0)
    while pq:
        visit(G, pq.put())

def visit(G, v):
    marked[v] = True
    for e in G.adj(v):
        w = e.other(v)
        if marked[w]:
            continue
        if e.weight() < distTo[w]:
            edgeTo[w] = e
            distTo[w] = e.weight()
            if pq.contains(w):
                pq.changeKey(w, distTo[w])
            else:
                pq.put(w, distTo[w])
