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
        res = []
        # are the nodes in the linked list always in order?
        # last num in nums doesn't have to connect to anything?

        curr = head
        while curr:
            if curr.val in nums:
                # case that value is last index
                if curr.val == nums[len(nums) -1]:
                    res.append([curr.val])
                    return len(res)
                # else
                elif curr.next and curr.next.val in nums:
                    res.append([curr.val, curr.next.val])
                    curr = curr.next.next
                # case where one number in nums, but next is not
                else:
                    curr = curr.next
            else:
                curr = curr.next

        return len(res)



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

print(sol.numComponents(head = n1, nums = [0, 2])) # 1? 