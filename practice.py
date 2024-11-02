# 701 insert into a BST

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        # go left
        elif val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        # go right
        elif val > root.val:
            root.right = self.insertIntoBST(root.right, val)

        return root


    

sol = Solution()
# 1, 2, 3, 4, 5, 7
tree = TreeNode(val = 4)
sol.insertIntoBST(tree, 2)
sol.insertIntoBST(tree, 7)
sol.insertIntoBST(tree, 1)
sol.insertIntoBST(tree, 3)
sol.insertIntoBST(tree, 5)

