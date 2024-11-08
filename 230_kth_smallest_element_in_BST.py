
'''
Kth Smallest Element in a BST
Leetcode #230
vsulli
8 November 2024

Given the root of a binary search tree, 
and an integer k, return the kth smallest 
value (1-indexed) of all the values of the nodes in the tree.
'''
from typing import Optional
# Definition for a binary tree node.
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
    

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        pass

sol = Solution()

tree = TreeNode(val = 3)
sol.insertIntoBST(tree, 1)
sol.insertIntoBST(tree, 4)
sol.insertIntoBST(tree, 2)

sol.kthSmallest(tree, 1)