# 701 - Insert into a BST

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val:int)->Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)

        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)

        return root
    

    def deleteNode(self, root: Optional[TreeNode], key: int)-> Optional[TreeNode]:
        if not root:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            curr = root.right
            while curr.left:
                curr = curr.left
            root.val = curr.val
            root.right = self.deleteNode(root.right, root.val)
        return root


sol = Solution()

root = TreeNode(4)

sol.insertIntoBST(root, 5)
sol.deleteNode(root, 4)
