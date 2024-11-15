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
        res = []
        q = collections.deque()
        if root:
            q.append(root)

        while q:
            level = []

            for i in range(len(q)):
                node = q.popleft()
                # don't need to check if the node val is not null here because the first value will always
                # be the root, which is guaranteed not to be null
                level.append(node.val)
                # here we check if a left and right exist, so if they were null they don't get added to the level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res
    


sol = Solution()

print(sol.levelOrder(root = [3,9,20,None,None,15,7]))