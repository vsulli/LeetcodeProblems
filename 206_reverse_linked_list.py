'''
Reverse Linked List
Leetcode # 206
vsulli
15 June 2024

Given the head of a singly linked list, 
reverse the list, and return the reversed list
'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            tmp_next = curr.next
            curr.next = prev
            prev = curr
            curr = tmp_next

        return prev

