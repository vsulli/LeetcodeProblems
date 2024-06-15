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
        # pos - just need to check that none of the next pointers are -1?
        seen = set() # number: next number
        curr = head
        # while there is a pointer, increment
        while curr:
            # if you see same number, return True
            if curr.next in seen:
                return True
            seen.add(curr)
            curr = curr.next

        return False


sol = Solution()

l1 = ListNode(3)
l1.next = ListNode(2)
l1.next = ListNode(0)
l1.next = ListNode(4)
l1.next = ListNode(2)

print(sol.hasCycle())