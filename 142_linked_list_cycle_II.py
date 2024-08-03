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
        # first use Floyd's Algorithm to detect a cycle with fast and slow pointers
        slow = head
        fast = head.next
        while fast and slow != fast:
            slow = slow.next
            fast = fast.next.next

         # if no cycle detected, return None
        if fast == None:
            return None
        
        # then create a second slow pointer starting at the beginning and
        # where both slow pointers meet is the intersection
        slow2 = head
        while True:
            print("slow: " + str(slow.val))
            print("slow2: " + str(slow2.val))
            print("------")
            slow = slow.next
            slow2 = slow2.next
            if slow.val == slow2.val:
                return slow.val




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

'''
n5 = ListNode(-1)
print(sol.detectCycle(n5))
'''