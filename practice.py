# 144 binary tree preorder traversal

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

from typing import Optional, List

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
        # navigate to where node to delete is 
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # if not left or right child
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            
            # go to min of right subtree (leftmost)
            curr = root.right
            while curr.left:
                curr = curr.left
            root.val = curr.val
            root.right = self.deleteNode(root.right, root.val)

        return root
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def preorder(root):
            if root:
                res.append(root.val)
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return res

sol = Solution()

root = TreeNode(5)
sol.insertIntoBST(root, 3)
sol.insertIntoBST(root, 6)
sol.insertIntoBST(root, 2)
sol.insertIntoBST(root, 4)
sol.insertIntoBST(root, 7)

print(sol.deleteNode(root, 3))

print(sol.preorderTraversal(root))