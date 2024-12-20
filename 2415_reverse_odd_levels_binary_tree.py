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
        # add root to queue
        # for each level, pop all nodes in the queue (represents current level)
        # push children tot he queue for the next level
        # for odd levels, collect values of nodes in an array, reverse array, then update nodes' values
        if not root:
            return None # empty tree
        queue = [root] 
        level = 0

        while queue:
            size = len(queue)
            current_level_nodes = []

            # process nodes at current level
            for _ in range(size):
                node = queue.pop(0)
                current_level_nodes.append(node)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # reverse nodes if current level is odd
            if level % 2 == 1:
                left, right = 0, len(current_level_nodes) - 1
                while left < right:
                    tmp = current_level_nodes[left].val
                    current_level_nodes[left].val = current_level_nodes[right].val
                    current_level_nodes[right].val = tmp
                    left += 1
                    right -= 1
            level += 1
        return root 


sol = Solution()
