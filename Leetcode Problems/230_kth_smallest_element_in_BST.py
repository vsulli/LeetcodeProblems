
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
        # iterative stack solution
        # start at root, don't visit yet, go as left as possible
        n = 0 #number of elements visited 
        stack = []
        cur = root

        while cur or stack:
            while cur:
                # add current to stack
                stack.append(cur)
                # keep going left
                cur = cur.left
            # reach NULL
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val # have processed kth value
            # go to right subtree
            cur = cur.right



sol = Solution()

tree = TreeNode(val = 3)
sol.insertIntoBST(tree, 1)
sol.insertIntoBST(tree, 4)
sol.insertIntoBST(tree, 2)

print(sol.kthSmallest(tree, 1)) # 1 

tree2 = TreeNode(val = 5)

sol.insertIntoBST(tree2, 5)
sol.insertIntoBST(tree2, 3)
sol.insertIntoBST(tree2, 6)
sol.insertIntoBST(tree2, 2)
sol.insertIntoBST(tree2, 4)
sol.insertIntoBST(tree2, 1)

print(sol.kthSmallest(tree2, 3)) # 3