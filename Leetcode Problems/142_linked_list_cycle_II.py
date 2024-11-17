'''
Find the Duplicate Number
Leetcode # 2678
vsulli
2 August 2024

Given an array of integers nums 
containing n + 1 integers where 
each integer is in the range 
[1, n] inclusive.

There is only one repeated number 
in nums, return this repeated number.

You must solve the problem without 
modifying the array nums and uses 
only constant extra space.
'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return

        # first use Floyd's Algorithm to detect a cycle with fast and slow pointers
        # they will land on same node, but won't be intersection
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break

         # if no cycle detected, return None
        if not fast.next or not fast.next.next:
            return None
         
        # then create a second slow pointer starting at the beginning and
        # where both slow pointers meet is the intersection
        slow2 = head
        while slow.next:
            if slow == slow2:
                return slow
            slow = slow.next
            slow2 = slow2.next

sol = Solution()

n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(0)
n4 = ListNode(-4)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n2

print(sol.detectCycle(n1))

n5 = ListNode(-1)
print(sol.detectCycle(n5))
