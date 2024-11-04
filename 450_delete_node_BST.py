
'''
Delete node in a BST
Leetcode #450
vsulli
29 October 2024

Given a root node reference of a BST and a key, 
delete the node with the given key in the BST. 
Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
'''
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
        
        # go left
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)

        # go right
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)

        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        # search left
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        # search right
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        # found node to delete
        else:
            # no left child
            if not root.left:
                return root.right
            # no right child
            if not root.right:
                return root.left
            
            # TODO learn this section down

            cur = root.right
            # find min of right subtree
            while cur.left:
                cur = cur.left

            # set new root value
            root.val = cur.val
            root.right = self.deleteNode(root.right, root.val)
        return root



    
sol = Solution()


tree = TreeNode(val = 4)
sol.insertIntoBST(tree, 2)
sol.insertIntoBST(tree, 7)
sol.insertIntoBST(tree, 1)
sol.insertIntoBST(tree, 3)
sol.insertIntoBST(tree, 5)

print(sol.deleteNode(root = tree, key = 3))