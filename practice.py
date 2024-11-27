# 102 Binary Tree Level Order Traversal

class TreeNode:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
import collections
class Solution:
    def levelOrder(self, root: Optional[TreeNode])-> Optional[TreeNode]:
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
                
        return res

sol = Solution()

