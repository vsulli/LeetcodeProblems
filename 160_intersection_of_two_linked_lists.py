'''
Intersection of Two Linked Lists
Leetcode # 160
vsulli
19 June 2024

Given the heads of two singly linked-lists
headA and headB, return the node at which
the two lists intersect.
If the two linked lists have no intersection, return null
'''

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # to improve efficiency

        currA = headA
        currB = headB
        while currA != currB:
            currA = currA.next if currA else headB
            currB = currB.next if currB else headA
        return currA
        

sol = Solution()

a1 = ListNode(1)
a2 = ListNode(2)
c1 = ListNode(1)
c2 = ListNode(2)
c3 = ListNode(3)
b1 = ListNode(1)
b2 = ListNode(2)
b3 = ListNode(3)

a1 = ListNode(2)
a2 = ListNode(6)
a3 = ListNode(4)

b1 = ListNode(1)
b2 = ListNode(5)

a1.next = a2
a2.next = c1
c1.next = c2
c2.next = c3
b1.next = b2
b2.next = b3
b3.next = c1

print(sol.getIntersectionNode(a1, b1))
a1.next = a2
a2.next = a3

b1.next = b2
b2.next = None

print(sol.getIntersectionNode(a1, b1))