
'''
Insert into a Binary Search Tree
Leetcode #701
vsulli
26 October 2024


'''
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # if value is less than value of current node, go left
        # apply same function to that new node to determine what to do
        # else go right
        if val < root.val:
            # no node to left
            if root.left is None:
                root.left = TreeNode(val)
            else:
                root.left = self.insertIntoBST(root, val)
        else:
            if root.right is None:
                root.right = TreeNode(val)
            else:
                root.right = self.insertIntoBST(root, val)



sol = Solution()

tree = TreeNode(val = 4)
sol.insertIntoBST(tree, 2)
sol.insertIntoBST(tree, 7)
sol.insertIntoBST(tree, 1)
sol.insertIntoBST(tree, 3)
sol.insertIntoBST(tree, 5)



