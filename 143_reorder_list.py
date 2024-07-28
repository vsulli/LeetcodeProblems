'''
Reorder List
Leetcode # 143
vsulli
28 July 2024

You are given the head of a singly linked list. 
l0 -> l1 -> ... -> ln -1 -> ln

Reorder the list to be on the following form:
l0 -> ln->l1->ln-1...

You may not modify the values in the list's nodes, only the 
nodes themselves may be changed
'''



from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # take one from front, take one from back
        size = 0
        curr = head
        temp = curr

        while curr:
            size += 1
            curr = curr.next

        count = 0
        front = 2
        back = size
        left = False
        
        while count != size:
            if left:

            else:
                while :
                    
            



        return head
        
sol = Solution()

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)

n1.next = n2
n2.next = n3
n3.next = n4

print(sol.reorderList(n1))
