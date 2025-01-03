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

    def get(self, key: int):
        if key in self.cache:
            # one just accessed becomes MRU
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1 

    def put(self, key: int, value: int)-> None:
        if key in self.cache:
            self.remove(self.cache[key])
        # create new node and insert into cache
        self.cache[key] = Node(key, value)
        # insert node into linked list
        self.insert(self.cache[key])
        # check capacity
        if len(self.cache) > self.cap:
            # delete LRU
            lru = self.left.next
            self.remove(lru) # remove from linked list
            del self.cache[lru.key] # remove from hashmap


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)