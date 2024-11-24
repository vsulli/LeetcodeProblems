# 701 Insert into a Binary Search Tree
# 450 Delete ndoe in a BST

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
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                curr = root.right
                while curr.left:
                    curr = curr.left
                root.val = curr.val
                root.right = self.deleteNode(root.right, root.val)
        return root

root = TreeNode(4)
sol = Solution()

sol.insertIntoBST(root, 2)
sol.insertIntoBST(root, 7)
sol.insertIntoBST(root, 1)
sol.insertIntoBST(root, 3)
sol.insertIntoBST(root, 5)

sol.deleteNode(root, 1)