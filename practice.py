# 450 delete node in a bst

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

from typing import Optional
class Solution:
    def insertIntoBST(self, root : Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # base case
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        # navigate to where the node would be
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            # if not left child
            if not root.right:
                return root.left
            # if not right child
            elif not root.left:
                return root.right
            # go to minimum of right subtree (which will be leftmost)
            curr = root.right
            while curr.left:
                curr = curr.left
            # have to set new value and delete recursively
            root.val = curr.val
            root.right = self.deleteNode(root.right, root.val)

        return root


sol = Solution()

root = TreeNode(5)
sol.insertIntoBST(root, 3)
sol.insertIntoBST(root, 6)
sol.insertIntoBST(root, 2)
sol.insertIntoBST(root, 4)
sol.insertIntoBST(root, 7)

print(sol.deleteNode(root, 3))