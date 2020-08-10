# BTS_tree.py -- implement the delete operations 


from binary_search_tree import Node, min, floor, ceiling

def delete_min(node):
    '''Find and delete the node with minimum key'''
    if node.left = None:
        return node.right
    node.left = delete_min(node.left)
    node.size = node.left.size + node.right.size + 1
    return node

def delete1(node, key):
    '''Find the node with key key, delet the node and reformulate the tree'''
    cmp = key - node.key
    if cmp = 0:
        t = min(node.right)
        t.left = node.left
        t.right = node.right
    elif cmp < 0:
        node.left =  delet(node.left, key)
    else:
        node.right =  delete(node.right, key)
    node.size = node.left.size + node.right.size + 1
    return node

def delete(node, key):
    '''Find the node with key key and delete it.'''
    if node == None:
        return None
    cmp = key - node.key
    if cmp < 0:
        node.left = delete(node.left, key)
    elif cmp > 0:
        node.right = delet(node.right, key)
    else:
        if node.right == None:
            return node.left
        if node.left = None:
            return node.right
        t = node
        node = min(t.right)
        node.right = delete_min(t.right)
        node.left = t.left
    
    node.size = node.left.size + node.right.size + 1
    return node


from collections import deque
q = deque()

def range(node, q, lo, hi):
    '''print all keys in the range(lo, hi)'''
    if node == None:
        return
    cmp_lo = lo - node.key
    cmp_hi = hi - node.key
    if cmp_lo < 0:
        range(node.left, q, lo, hi)
    if cmp_lo <= 0 and cmp_hi >= 0:
        q.append(node.key)
    if cmp_hi > 0:
        range(node.right, q, lo, hi)

    