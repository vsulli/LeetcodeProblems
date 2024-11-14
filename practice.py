# 102 Binary Tree Level Order Traversal

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

from typing import Optional, List
import collections

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = collections.deque([root])
        res = []
        # process tree level by level
        while q:
            level = []
            for _ in range(len(q)): # iterate over  current level
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # append level items 
            res.append(level)

        return res


sol = Solution()

print(sol.levelOrder(root = [3,9,20,None,None,15,7]))