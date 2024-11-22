# 450 delete node in a BST
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode],key: int)->Optional[TreeNode]:
        if not root:
            return root
        
        # if key < root 
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        # if key > root
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            # if no left child
            # if no right child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
    
            # find min of right subtree
            curr = root.right
            while curr.left:
                curr = curr.left
            root.val = curr.val
            root.right = self.deleteNode(root.right, root.val)
        return root

