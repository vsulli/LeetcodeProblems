# 146 LRU Cache 
# Practice Submission
# 26 December 2024

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # key: node

        # initialize two dummy nodes pointing to each other
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left 

    # helper functions applied to linked list
    # remove node from list
    def remove(self, node):
        # get node's prev and next
        prev, nxt = node.prev, node.next

        # updating pointers of one behind and one in front
        prev.next, nxt.prev = nxt, prev 

    # insert at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node 
        node.next, node.prev = nxt, prev

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
