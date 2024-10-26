
'''
Insert into a Binary Search Tree
Leetcode #701
vsulli
26 October 2024


'''
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        pass

sol = Solution()


tree = TreeNode(val = 4)
tree.left = TreeNode(2)
tree.right = TreeNode(7)

