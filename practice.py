# 450 delete node bst

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def printPreOrder(self, root: Optional[TreeNode]):
        if not root:
            return
        print(root.val)
        self.printPreOrder(root.left)
        self.printPreOrder(root.right)

    def printInOrder(self, root: Optional[TreeNode]):
        if not root:
            return
        
        self.printInOrder(root.left)
        print(root.val)
        self.printInOrder(root.right)

    def printPostOrder(self, root: Optional[TreeNode]):
        if not root:
            return
        self.printPostOrder(root.left)
        self.printPostOrder(root.right)
        print(root.val)

    def deleteNode(self, root: Optional[TreeNode], key: int)-> Optional[TreeNode]:
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

sol.printPreOrder(tree)

sol.deleteNode(tree, 1) # delete 1
print("--------------")

sol.printPreOrder(tree)