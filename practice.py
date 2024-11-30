# 701

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        elif val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        elif val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        return root

sol = Solution()

root = TreeNode(4)
sol.insertIntoBST(root, val = 2)
sol.insertIntoBST(root, val = 7)
sol.insertIntoBST(root, val = 1)
sol.insertIntoBST(root, val = 3)
print(sol.insertIntoBST(root, val = 5))