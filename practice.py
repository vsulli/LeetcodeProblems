# 15 August 2024

# Leetcode # 146 - LRU Cache
# uses a hashmap and nodes

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        # left = LRU, right = MRU
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    
    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    
    # insert at right
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
            # remove from list and delete from hashmap
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

my_cache =  LRUCache(2) # initializes cache with 2 

my_cache.put(1, 10)  # cache: {1=10}
print(my_cache.get(1))      # return 10
my_cache.put(2, 20)  # cache: {1=10, 2=20}
my_cache.put(3, 30)  # cache: {2=20, 3=30}, key=1 was evicted
print(my_cache.get(2))     # returns 20 
print(my_cache.get(1))      # return -1 (not found)