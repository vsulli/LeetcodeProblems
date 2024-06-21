# TODO Incomplete. Draw out all scenarios. Need solution without extra memory
'''
Merge Two Sorted Lists
Leetcode # 21
vsulli
19 June 2024

You are given the heads of two sorted linked lists
list1 and list2

Merge the two lists into one sorted list. The list
should be made by splicing together the nodes of the 
first two lists

Return the head of the merged linked list
'''

# Definition for singly-linked list.
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # set pointers to beginning of both lists
        # compare those nodes
        # if same, take list1 first, then add list2, increment
        # else take lower
            # increment that list
        # keep going until both are None

        head = ListNode() # make dummy node for head of list

        currA = list1
        currB = list2

        while currA or currB:
             # same value - apply a first
            if currA.val == currB.val or currA.val < currB.val:
                tempA = currA.next
                currA.next = currB
                tempB = currB.next
                currA.next.next = tempA
                currB = tempB
            elif currB.val < currA.val:
                tempA = currA.next

            


        # return head.next as beginning of list
        


sol = Solution()

a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(4)

b1 = ListNode(1)
b2 = ListNode(3)
b3 = ListNode(4)

a1.next = a2
a2.next = a3

b1.next = b2
b2.next = b3

sol.mergeTwoLists()
