
'''
Construct Binary Tree from
Preorder and Inorder Traversal
Leetcode #105
vsulli
9 November 2024

Given two integer arrays preorder and 
inorder where preorder is the preorder 
traversal of a binary tree and inorder 
is the inorder traversal of the same tree, 
construct and return the binary tree.

'''
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # first of preorder list will ALWAYS be main root
            # can look that value up in inorder to split into left and right subtree lengths
        # second of preorder list will ALWAYS be root of left subtree
        # every value to left of root will be in left subtree and every value to right
        # will be in right subtree
        # partition preorder array  into indices for left and right

        # recursive algorithm base case
        # no nums
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0]) # get index of root in inorder array 
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid]) # build subtree
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root

sol = Solution()

sol.buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])
sol.buildTree(preorder = [-1], inorder = [-1])