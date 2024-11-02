# 450 delete node bst

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int)-> Optional[TreeNode]:
        # if no root, return root
        if not root:
            return root

        # navigate to where value would be
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        elif key > root.val:
            root.left = self.deleteNode(root.right, key)

        
        else:
            if not root.left:
                return root.right
            elif not root.left:
                return root.left 
            
            cur = root.right 
            while cur:
                cur = cur.right
            
        
        return root


        # if no left child
        # if no right child

        # cur pointer
        # recursively call delete?


        return root
        



    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        # go left
        elif val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        # go right
        elif val > root.val:
            root.right = self.insertIntoBST(root.right, val)

        return root


    

sol = Solution()
# 1, 2, 3, 4, 5, 7
tree = TreeNode(val = 4)
sol.insertIntoBST(tree, 2)
sol.insertIntoBST(tree, 7)
sol.insertIntoBST(tree, 1)
sol.insertIntoBST(tree, 3)
sol.insertIntoBST(tree, 5)

sol.deleteNode(tree, 1) # delete 1