# binary_search.py -- use two arrays to store keys(ordered) and values

keys = []
values = []
N = len(keys)

def rank(key, lo, hi):
    '''recursive binary rank'''
    if hi < lo:
        return 
    mid = int(lo + (hi-lo)/2)
    cmp = key - keys[mid]
    if cmp < 0:
        rank(key, lo, mid-1)
    elif cmp > 0:
        rank(key, mid+1, hi)
    else:
        return mid

def rank_i(key):
    '''iterative binary rank'''
    while hi < lo:
        mid = int(lo + (hi-lo)/2)
        cmp = key - keys[mid]
        if cmp < 0:
            hi = mid - 1
        elif cmp > 0:
            lo = mid + 1
        else:
            return mid
    return lo

def get(key):
    if N == 0:
        return None
    i = rank(key)
    if i < N and keys[i] == key:
        return values[i]
    return None

def put(key, val):
    i = rank(key)
    if i < N and keys[i] == key:
        values[i] = val
        return 
    keys.append(key), values.append(val)
    for j in range(N, i, -1):
        keys[j] = keys[j-1]
        values[j] = values[j-1]
    keys[i] = key
    values[i] = val
    N += 1
