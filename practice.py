# 450 Delete Node in a BST

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # iterative solution
        if not root:
            return TreeNode(val)
        
        cur = root
        while True:
            if val > cur.val:
                if not cur.right:
                    cur.right = TreeNode(val)
                    return root
                cur = cur.right
            else:
                if not cur.left:
                    cur.left = TreeNode(val)
                    return root
                cur = cur.left

    def printTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left = self.printTree(root.left)
            print(root.val)
            root.right = self.printTree(root.right)


sol = Solution()
# 1, 2, 3, 4, 5, 7
tree = TreeNode(val = 4)
sol.insertIntoBST(tree, 2)
sol.insertIntoBST(tree, 7)
sol.insertIntoBST(tree, 1)
sol.insertIntoBST(tree, 3)
sol.insertIntoBST(tree, 5)


sol.printTree(tree)