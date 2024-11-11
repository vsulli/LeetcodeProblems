'''
Binary Tree Level Order Traversal
Leetcode # 102
vsulli
11 November 2024


'''

from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass

sol = Solution()

root = TreeNode(3)


print(sol.levelOrder(root))