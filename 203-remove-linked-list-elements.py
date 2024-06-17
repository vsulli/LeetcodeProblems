'''
Remove Linked List Elements
Leetcode # 203
vsulli
17 June 2024

Given the head of a linked list and an integer val, remove
all the nodes of the linked list that has Node.val == val,
and return the new head
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def printList(head: Optional[ListNode]):
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next
    print('---------')


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
             return []
        # initialize pointer as first node
        curr = head

        # first val is val to delete
        if curr.val == val:
                temp = curr.next
                head = temp

        #curr = head
        while curr:
            if curr.next and curr.next.val == val:
                curr.next = curr.next.next
            curr = curr.next
        return head

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(6)
l4 = ListNode(3)
l5 = ListNode(4)
l6 = ListNode(5)
l7 = ListNode(6)

l8 = ListNode(7)
l9 = ListNode(7)
l10 = ListNode(7)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l7

l8.next = l9
l9.next = l10

sol = Solution()

'''
printList(l1)
l1 = sol.removeElements(l1, 6)
printList(l1)
print(sol.removeElements(head = [], val = 1))
'''
printList(l8)
l8 = sol.removeElements(l8, 7)
printList(l8)