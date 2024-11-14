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
        # timothy h chang
        # dfs
        d = collections.defaultdict(list)
        
        def dfs(node, level):
            if not node: return
            d[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        dfs(root, 0)

        return list(d.values())

sol = Solution()

print(sol.levelOrder(root = [3,9,20,None,None,15,7]))