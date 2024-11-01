# 450 Delete Node in a BST

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        # find node to delete

        # go to right
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        # go to left
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        # found node to delete
        else:
            # left of root is null?
            # return right
            if not root.left:
                return root.right

            elif not root.right:
                return root.left
        
            # find minimum of right subtree
            cur = root.right
            while cur.left: # stop at a valid node
                cur = cur.left 
            # by end of loop cur points at min val of right subtree
            root.val = cur.val
            root.right = self.deleteNode(root.right, root.val) # deleting now duplicate value of cur val/root val in right subtree
        return root


sol = Solution()
