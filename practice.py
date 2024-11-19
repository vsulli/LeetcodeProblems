# 144 binary tree preorder traversal

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

from typing import Optional, List
import collections

class Solution:
    def insertIntoBST(self, root:Optional[TreeNode], value: int)->Optional[TreeNode]:
        if not root:
            return TreeNode(value)
        if value < root.val:
            root.left = self.insertIntoBST(root.left, value)
        elif value > root.val:
            root.right = self.insertIntoBST(root.right, value)
        return root
    def deleteNode(self, root:Optional[TreeNode], key:int)->Optional[TreeNode]:
        if not root:
            return root 

        # navigate to area of key
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # if no left child
            if not root.left:
                return root.right

            # if no right child
            if not root.right:
                return root.left

            # on right subtree, find min
            curr = root.right
            while curr.left:
                curr = curr.left 
            root.val = curr.val
            root.right = self.deleteNode(root.right, root.val)
        
        return root


    
        
            
            
            

sol = Solution()

root = TreeNode(5)
sol.insertIntoBST(root, 3)
sol.insertIntoBST(root, 6)
sol.insertIntoBST(root, 2)
sol.insertIntoBST(root, 4)
sol.insertIntoBST(root, 7)

print(sol.deleteNode(root, 3))
