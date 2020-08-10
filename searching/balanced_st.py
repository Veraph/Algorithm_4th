# Red and Black balanced search tree
class Node():
    def __init__(self, key, val, size, color='red', left=None, right=None)
        self.key = key
        self.value = value
        self.size = size
        self.left = left
        self.right = right
        self.color = color

def isRed(node):
    '''identify the color of the node(depend on the line pointing to the node)'''
    return node.color == 'red'

def rotate_left(node):
    '''rotate the consecutive red links to right'''
    t = node.left
    node.right = t.left
    t.left = node
    t.color = node.color
    node.color = 'red'
    t.size = node.size
    node.size = node.left.size + node.right.size + 1
    return t

def rotate_right(node):
    '''rotate the right red link to left'''
    t = node.left
    node.left = t.right
    t.right = node
    t.color = node.color
    node.color = 'red'
    t.size = node.size
    node.size = node.left.size + node.right.size + 1
    return t

def flip_colors(node):
    '''flip colors if both of the node's child is red'''
    node.color = 'red'
    node.left.color = 'black'
    node.right.color = 'black'

def put(node, key, val):
    '''change the node with key's value to val, if no such key, create a new node with that key and val'''
    if node == None:
        return Node(key, val, 1)
    cmp = key - node.key
    if cmp == 0:
        node.value = val
    elif cmp > 0:
        node.right = put(node.right, key, val)
    else:
        node.left = put(node.left, key, val)

    if isRed(node.right) and !isRed(node.left):
        rotate_left(Node)
    if isRed(node.left) and isRed(node.left.left):
        rotate_right(Node)
    if isRed(node.left) and isRed(node.right):
        flip_colors(node)

    node.size = 1 + node.left.size + node.right.size
    return node

def moveRedLeft(node):
    flip_colors(node)
    if isRed(node.right.left):
        node.right = rotate_right(node.right)
        node = rotate_left(node)
    return node

def moveRedRight(node):
    flip_colors(node)
    if !isRed(node.left.left):
        node = rotate_right(node)
    return node

def balance(node):
    if isRed(node.right):
        node = rotate_left(node)

def deleteMin(node):
    if node.left = None:
        return None
    if !isRed(node.left) and !isRed(node.left.left):
        node = moveRedLeft(node)
    node.left = deleteMin(node.left)
    return balance(node)

if !isRed(root.left) and !isRed(root.right):
    root.color = 'red'
root = deleteMin(root)
if root:
    root.color = 'black'


def deleteMax(node):
    if isRed(node.left):
        node = rotate_right(node)
    if node.right == None:
        return None
    if !isRed(node.right) and !isRed(node.right.left):
        node = moveRedRight(node)
    node.right = deleteMax(node.right)
    return balance(node)

if !isRed(root.left) and !isRed(root.right):
    root.color = 'red'
root = deleteMax(root)
if root:
    root.color = 'black'


def delete(node, key):
    if key - node.key < 0:
        if !isRed(node.left) and !isRed(node.left.left):
            node = moveRedLeft(node)
        node.left = delete(node.left, key)
    
    else:
        if isRed(node.left):
            node = rotate_right(node)
        if key - node.key == 0 and node.right == None:
            return None
        if !isRed(node.right) and !isRed(node.right.left):
            node = moveRedRight(node)
        if key - node.key == 0:
            node.val = get(node.right, min(node.right).key)
            node.key = min(node.right).key
            node.right = deleteMin(node.right)
        
        else:
            node.right = delete(node.right, key)
    return balance(node)

if !isRed(root.left) and !isRed(root.right):
    root.color = 'red'
root = delete(root, key)
if root:
    root.color = 'black'



