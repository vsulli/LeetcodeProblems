# 701 Insert into a Binary Search Tree
from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root : Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # no root node
        if not root:
            return TreeNode(val)

        # need to go left
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)

        # need to go right
        else:
            root.right = self.insertIntoBST(root.right, val)
            
        return root
    
root = TreeNode(4)

sol = Solution()

sol.insertIntoBST(root, 2)
sol.insertIntoBST(root, 7)
sol.insertIntoBST(root, 1)
sol.insertIntoBST(root, 3)
sol.insertIntoBST(root, 5)