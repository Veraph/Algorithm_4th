# priority_queue.py -- implement related pq operations

def exch(i, j):
    temp = pq[i]
    pq[i] = pq[j]
    pq[j] = temp

def less(i, j):
    if pq[i] < pq[j]:
        return True
    else:
        return False

def swim(k):
    '''bottom-up reheapify implementation'''
    while k > 1 and less(k/2, k):
        exch(int(k/2), k)
        k = int(k/2)

def sink(k):
    '''Top-down reheapify implementation'''
    while 2*k <= N:
        j = 2*k
        if j < N and less(j, j+1):
            j += 1
        if !less(k, j):
            break
        exch(k, j)
        k = j
