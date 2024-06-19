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
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # given the head of list a and b
        # need two pointers to the heads of each list
        # loop through, comparing the value of that pointer of each list
        # if they match then return that node

sol = Solution()

a1 = ListNode(1)
a2 = ListNode(2)
c1 = ListNode(1)
c2 = ListNode(2)
c3 = ListNode(3)
b1 = ListNode(1)
b2 = ListNode(2)
b3 = ListNode(3)

a1.next = a2
a2.next = c1
c1.next = c2
c2.next = c3
b1.next = b2
b2.next = b3
b3.next = c1

print(sol.getIntersectionNode(a1, b1))