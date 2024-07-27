# 817 practice

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def linkedListValues(self, head: Optional[ListNode]) -> list[int]:
        res = []
        curr = head

        while curr:
            res.append(curr.val)
            curr = curr.next

        return res




n1 = ListNode("a")
n2 = ListNode("b")
n3 = ListNode("c")
n4 = ListNode("d")

n1.next = n2
n2.next = n3
n3.next = n4

sol = Solution()

print(sol.linkedListValues(n1))
