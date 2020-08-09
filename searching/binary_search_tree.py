# BinarySearchTree.py -- Implementation

class Node(object):
    def __init__(self, key, value, size, left=None, right=None):
        self.key = key
        self.value = value
        self.size = size
        self.left = left
        self.right = right


d = Node(5, 4, 1)
a = Node(2, 1, 1)
c = Node(4, 3, 3, a, d)

def size(node):
    if node == None:
        return 0
    else:
        return node.size

def get(node, key):
    '''find out whether key exists in subtrees rooted in x and return its' value'''
    if node == None:
        return None
    cmp = key - node.key
    if cmp > 0:
        get(node.right, key)
    elif cmp < 0:
        get(node.left, key)
    else:
        return node.value

def put(node, key, val):
    '''change the node with key's value to val, if no such node, create one'''
    if node == None:
        return Node(key, val, 1)
    cmp = key - node.key
    if cmp > 0:
        node.right = put(node.right, key, val)
    elif cmp < 0:
        node.left = put(node.left, key, val)
    else:
        node.value = val
    node.size = size(node.left) + size(node.right) + 1

def min(node):
    '''find the smallest key in the tree, call by min(root)'''
    if node.left == None:
        return node.key
    else:
        return min(node.left)

def max(node):
    '''find the biggest key in the tree, call by max(root)'''
    if node.right == None:
        return node.key
    else:
        return max(node.right)

def floor(node, key):
    '''find the floor of a given key(the biggest key smaller or equal to the given key), call by floor(root, key)'''
    if node == None:
        return None
    cmp = key - node.key
    if cmp == 0:
        return node.key
    if cmp < 0:
        return floor(node.left, key)
    
    t = floor(node.right, key)
    if t != None:
        return t
    else:
        return node.key

def ceiling(node, key):
    '''find the ceiling of a given key(the smallest key bigger or equal to the given key), call by ceiling(root, key)'''
    if node == None:
        return None
    cmp = key - node.key
    if cmp == 0:
        return node.key
    if cmp > 0:
        return floor(node.right, key)
    
    t = floor(node.left, key)
    if t != None:
        return t
    else:
        return node.key


def rank(node, key):
    '''return the rank of a given key'''
    if node == None:
        return 0
    if node.key == key:
        return node.left.size
    elif node.key > key:
        return rank(node.left, key)
    else:
        return 1 + node.left.size + rank(node.right, key) 

def selection(node, rank):
    '''find the node with rank'''
    if node == None:
        return None
    t = node.left.size
    if t > rank:
        return selection(node.left, rank)
    elif t < rank:
        return selection(node.right, rank-t-1)
    else:
        return node
print()