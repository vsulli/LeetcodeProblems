# 146 LRU Cache - Learning

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

    # insert linked list
    def insert(self, node):
        prv, nxt = self.right.prev, self.right
        prv.next = nxt.prev = node 
        node.next, node.prev = nxt, prv

    # remove linked list
    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next = nxt
        nxt.prev = prv 

    def get(self, key: int):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            # update to MRU
            return self.cache[key].val
        return -1 

    def put(self, key: int, value: int)-> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        # insert node into cache
        self.insert(self.cache[key])
        # check capacity
        if len(self.cache) > self.cap:
            # remove from list and delete LRU from hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


