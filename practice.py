# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        def inorder(root):
            if root:
                root.left = inorder(root.left)
                res.append(root.val)
                root.right = inorder(root.right)
        inorder(root)
        return res

