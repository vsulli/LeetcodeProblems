
'''
Binary Tree Postorder Traversal
Leetcode #145
vsulli
7 November 2024

Given the root of a binary tree, return 
the postorder traversal of its nodes' values.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
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
 
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []

        def postorder(root):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)
        postorder(root)

        return res

 
sol = Solution()

tree = TreeNode(val = 1)
sol.insertIntoBST(tree, 2)
sol.insertIntoBST(tree, 3)

print(sol.postorderTraversal(tree))