
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
          pass
    
sol = Solution()

sol.buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])
sol.buildTree(preorder = [-1], inorder = [-1])