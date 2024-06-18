'''
Remove Duplicates from Sorted List
Leetcode # 83
vsulli
18 June 2024

Given the head of a sorted linked list, delete all duplicates
such that each element appears only once. Return the linked
list sorted as well
'''

#  Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList(head: ListNode):
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next
    print('----')

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        return curr

sol = Solution()

l1 = ListNode(1)
l2 = ListNode(1)
l3 = ListNode(2)

l4 = ListNode(1)
l5 = ListNode(1)
l6 = ListNode(2)
l7 = ListNode(3)
l8 = ListNode(3)

l1.next = l2
l2.next = l3

l4.next = l5
l5.next = l6
l6.next = l7
l7.next = l8


new_list = sol.deleteDuplicates(l1)
printList(new_list)

new_list = sol.deleteDuplicates(l4)
printList(new_list)