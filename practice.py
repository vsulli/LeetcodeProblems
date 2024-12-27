# 146 LRU Cache - Learning

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # key: node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left 

        
