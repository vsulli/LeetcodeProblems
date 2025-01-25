# 146 LRU Cache

class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev=self.next = None 

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left 

    def remove(self, node: Node):
        pass

    def insert(self, node: Node):
        pass

    def get(self, key: int):
        pass

    def put(self, key: int, value: int):
        pass

