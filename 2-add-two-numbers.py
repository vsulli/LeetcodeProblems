'''
Add Two Numbers
Leetcode # 2
vsulli
12 June 2024

Given two non-empty linked lists
representing two non-negative integers.
The digits are stored in reverse order, and each of their
nodes contains a single digit. Add the two numbers and return 
the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except
the number 0 itself.
'''


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # output can be in reversed order
        res = ListNode()
        # don't have a way of knowing which of l1 or l2 is longer
        # without iterating through all of them

        # pseudocode
        # while there is a current value on l1
        # add values and carry
        # if sum > 9 store new carry
        # else create node for result listnode

        carry = 0
        while l1:
            sum = l1.val + l2.val + carry 
            if sum > 9:
                carry = sum - 9
            else:
                res.val = sum


sol = Solution()

print(sol.addTwoNumbers(l1 = [2,4,3], l2 = [5,6,4])) # [7, 0, 8]

print(sol.addTwoNumbers(l1 = [0], l2 = [0])) # [0]

print(sol.addTwoNumbers(l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9])) # [8,9,9,9,0,0,0,1]