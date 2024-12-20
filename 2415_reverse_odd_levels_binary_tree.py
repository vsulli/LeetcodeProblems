''' 
Reverse Odd Levels of Binary Tree
Leetcode # 2415
vsulli
20 December 2024

Given the root of a perfect binary tree, 
reverse the node values at each odd level of the tree.

For example, suppose the node values at 
level 3 are [2,1,3,4,7,11,29,18], then it
should become [18,29,11,7,4,3,1,2].
Return the root of the reversed tree.

A binary tree is perfect if all parent 
nodes have two children and all leaves 
are on the same level.

The level of a node is the number of edges 
along the path between it and the root node.
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right
       
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # go through once in order and get the number of nodes at each level 
        # put in array
        # rebuild new tree and return?
        levels = []
        
        def levelOrderTraversal(root):
            if root:
                root.left = levelOrderTraversal(root.left)
                levels.append(root)
                root.right = levelOrderTraversal(root.right)
        levelOrderTraversal(root)
        
        print(levels)


sol = Solution()
