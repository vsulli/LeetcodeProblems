# 701 insert into a bst
# 450 delete node in a bst

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

from typing import Optional
class Solution:
    def insertIntoBST(self, root:Optional[TreeNode], value: int)->Optional[TreeNode]:
        if not root:
            return TreeNode(value)
        if value < root.val:
            root.left = self.insertIntoBST(root.left, value)
        elif value > root.val:
            root.right = self.insertIntoBST(root.right, value)
        return root

sol = Solution()

root = TreeNode(5)
sol.insertIntoBST(root, 3)
sol.insertIntoBST(root, 6)
sol.insertIntoBST(root, 2)
sol.insertIntoBST(root, 4)
sol.insertIntoBST(root, 7)

print(sol.deleteNode(root, 3))