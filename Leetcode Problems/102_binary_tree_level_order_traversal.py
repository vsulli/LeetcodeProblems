'''
Binary Tree Level Order Traversal
Leetcode # 102
vsulli
11 November 2024

Given the root of a binary tree, 
return the level order traversal of 
its nodes' values. (i.e., from left to 
right, level by level).
'''

from typing import Optional, List
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs 
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

root = TreeNode(3)


print(sol.levelOrder(root))