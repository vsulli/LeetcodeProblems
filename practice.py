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

    def insert(self, node):
        prv, nxt = self.right.prev, self.right
        node.prev, node.next = prv, nxt 
        prv.next = nxt.prev = node

    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv
        
    def get(self, key: int):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int):
        if key in self.cache:
            self.remove(self.cache[key]) # remove from linked list
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.left.next 
            # remove from linked list and cache
            self.remove(lru) # TODO
            del self.cache[lru.key] # TODO



