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

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

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