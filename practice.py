
# LRU Cache

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left 

    # insert into linked list
    def insert(self, node):
        prv, nxt = self.right.prev, self.right 
        node.prev, node.next = prv,nxt
        prv.next = nxt.prev = node 

    # remove from linked list
    def remove(self, node):
        prv, nxt = node.prev, node.next 
        prv.next, nxt.prev = nxt, prv 

