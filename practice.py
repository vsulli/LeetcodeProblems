# 817 practice

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: list[int]) -> int:
        curr = head
        res = 0
        flag = False

        while curr:
            if curr.val in nums:
                flag = True
                res +=1 
                while flag and curr.next:
                    curr = curr.next
                    flag = curr.val in nums
                curr = curr.next
            else:
                curr = curr.next

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
# how? orphan component - counts as connected to itself