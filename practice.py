# 450 delete node in a bst

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

from typing import Optional
class Solution:
    


sol = Solution()

root = TreeNode(5)
sol.insertIntoBST(root, 3)
sol.insertIntoBST(root, 6)
sol.insertIntoBST(root, 2)
sol.insertIntoBST(root, 4)
sol.insertIntoBST(root, 7)

print(sol.deleteNode(root, 3))