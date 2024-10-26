
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
        # iterative solution
        if not root:
            return TreeNode(val)
        
        cur = root
        while True:
            if val > cur.val:
                if not cur.right:
                    cur.right = TreeNode(val)
                    return root
                cur = cur.right
            else:
                if not cur.left:
                    cur.left = TreeNode(val)
                    return root
                cur = cur.left



sol = Solution()

tree = TreeNode(val = 4)
sol.insertIntoBST(tree, 2)
sol.insertIntoBST(tree, 7)
sol.insertIntoBST(tree, 1)
sol.insertIntoBST(tree, 3)
sol.insertIntoBST(tree, 5)



