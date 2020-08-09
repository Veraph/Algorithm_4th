# sequential_search.py -- in an unordered linked-list

class Node(object):
    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next

third = Node(2, 'c', None)
second = Node(1, 'b', third)
first = Node(0, 'a', second)

def get(key):
    x = first
    while x != None:
        if x.key == key:
            return x.value
        x = x.next
    return None

def put(key, val):
    x = first
    while x != None:
        if x.key == key:
            x.value = val
            return
        x = x.next
    new = Node(key, val, first)
    return

put(3, 'd')

