'''
Middle of the Linked List
Leetcode # 876
vsulli
17 June 2024

Given the head of a singly linked list, return the middle 
node of the linked list.

If there are two middle nodes, return the second middle node
'''

# Definition for singly-linked list.
from typing import Optional


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
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head.next

        # create two pointers, slow and fast
        # go through list
        # when fast reaches end, slow will be at middle
        # what happens when it's an even list?


sol = Solution()

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

print(sol.middleNode(l1))
printList(l1)
l5.next = l6

print(sol.middleNode(l1))
printList(l1)