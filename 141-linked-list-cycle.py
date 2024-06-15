'''
Linked List Cycle
Leetcode # 141
vsulli
15 June 2024

Given head, the head of a linked list, determine 
if the linked list has a cycle in it. 

A cycle exists if some node in the list can be reached again
by continuously following the next pointer
pos is not passed as a parameter
return true if there is a cycle, otherwise, return false
'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Floyd's Cycle Finding Algorithm / Hare-Tortoise Algorithm
        # initialize two pointers
        slow, fast = head, head
        
        # fast would reach null pointer before slow
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        # when fast reaches null pointer
        return False


sol = Solution()

l1 = ListNode(3)
l1.next = ListNode(2)
l1.next = ListNode(0)
l1.next = ListNode(4)
l1.next = ListNode(2)

print(sol.hasCycle())