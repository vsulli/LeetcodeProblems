''' 
Linked List Components
Leetcode # 817
vsulli
26 July 2024

You are given the head of a linked 
list containing unique integer values 
and an integer array nums that is a 
subset of the linked list values.

Return the number of connected components 
in nums where two values are connected 
if they appear consecutively in the 
linked list.
'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: list[int]) -> int:
        num_set = set(nums)

        res = 0
        flag = False
        while head:
            if head.val not in num_set and flag:
                res += 1
                flag = False
            elif head.val in num_set:
                flag = True
            head = head.next

        if flag:
            res += 1

        return res 



n1 = ListNode(0)
n2 = ListNode(1)
n3 = ListNode(2)
n4 = ListNode(3)

n1.next = n2
n2.next = n3
n3.next = n4

sol = Solution()

print(sol.numComponents(head = n1, nums = [0,1,3]))# 2
# [0, 1] and [3]

n5 = ListNode(4)
n4.next = n5
print(sol.numComponents(head = n1, nums = [0, 3, 1, 4])) # 2
# [0, 1] and [3,4]

n3.next = None

print(sol.numComponents(head = n1, nums = [0, 2])) # 2 according to output
# how?