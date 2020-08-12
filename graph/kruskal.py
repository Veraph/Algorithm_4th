# Kruskal.py -- An algorithm to find the MST
from queue import PriorityQueue
from collections import dequeue

def Kruskal(G):
    mst_pq = dequeue()
    min_pq = PriorityQueue()
    for e in G.edges():
        min_pq.put(e)
    uf = UF(V) # a union find data structure
    while min_pq and mst_pq.size() < V-1:
        e = min_pq.get()
        v = e.either()
        w = e.other(v)
        if uf.connected(v, w):
            continue
        uf.union(v, w)
        mst_pq.append(e)
