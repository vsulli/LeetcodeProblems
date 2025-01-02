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

    def remove(self, node): # linked list
        prv, nxt = node.prev, node.next 
        prv.next, nxt.prev = nxt, prv 

    def insert(self, node): # linked list
        prv, nxt = self.right.prev, self.right
        node.prev, node.next = prv, nxt
        prv.next = nxt.prev = node

    def get(self, key: int): 
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key]
        return -1

    def put(self, key: int, value: int):
        if key in self.cache:
            self.remove(self.cache[key]) # remove from linked list
        self.cache[key] = value  # insert into cache
        self.insert(key) # insert into linked list
        if len(self.cache) > self.cap:
            # get lru
            lru = self.left 
            # remove lru from cache and linked list
            self.remove(lru.val)
            del self.cache[lru]


