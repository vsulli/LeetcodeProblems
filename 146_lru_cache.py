'''
LRU Cache
Leetcode # 146
vsulli
27 June 2024

Design a data structure that follows the 
constraints of a Least Recently Used (LRU) 
cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU 
cache with positive size capacity.
int get(int key) Return the value of the key 
if the key exists, otherwise return -1.
void put(int key, int value) Update the value 
of the key if the key exists. Otherwise, add 
the key-value pair to the cache. If the number 
of keys exceeds the capacity from this operation, 
evict the least recently used key.
The functions get and put must each run in O(1) 
average time complexity.
'''

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # maps key to node

        # left = LRU, right = MRU
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev,node.next
        prev.next, nxt.prev = nxt, prev

    # insert node at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the list and delete the lru from hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)