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
        count = 0
        curr = head
        # while linked list exists
        while curr:
            prev = curr
            temp = curr.next
            # first node needs to point to none
            if count == 0:
                curr.next = None
                prev = curr
                curr = temp
                count +=1
            else:
                curr.next = prev
                prev = curr
                curr = temp
        return curr



