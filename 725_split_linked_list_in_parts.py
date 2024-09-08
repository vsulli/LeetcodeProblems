
'''
Split Linked List in Parts
Leetcode # 725
vsulli
8 September 2024

Given the head of a singly linked list and 
an integer k, split the linked list into k 
consecutive linked list parts.

The length of each part should be as equal 
as possible: no two parts should have a size 
differing by more than one. This may lead to 
some parts being null.

The parts should be in the order of occurrence 
in the input list, and parts occurring earlier 
should always have a size greater than or equal 
to parts occurring later.

Return an array of the k parts.
'''
from typing import List, Optional
import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # neetcode solution
        length, curr = 0, head

        while curr:
            curr = curr.next
            length += 1

        base_len, remainder = length // k, length % k
        curr = head
        res = []
        for i in range(k): # don't want to just iterate while curr, because we want null as well
            res.append(curr) # add first node to result list

            # n = 6, k = 2 
            # 1 -> 2-> 3->     4-> 5-> 6-> 
            for j in range(base_len - 1 + (1 if remainder else 0)): # want to iterate to node before last node (-1)
                if not curr: break # null pointer
                curr = curr.next
            remainder -= (1 if remainder else 0)
            # end of current part - set equal to None
            if curr:
                curr.next, curr = None, curr.next # instead of temporary variable

        return res


sol = Solution()

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)

n1.next = n2
n2.next = n3

print(sol.splitListToParts(head = n1, k = 5))
# Output: [[1],[2],[3],[],[]]

n4 = ListNode(1)
n5 = ListNode(2)
n6 = ListNode(3)
n7 = ListNode(4)
n8 = ListNode(5)
n9 = ListNode(6)
n10 = ListNode(7)
n11 = ListNode(8)
n12 = ListNode(9)
n13 = ListNode(10)

n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n9
n9.next = n10
n10.next = n11
n11.next = n12
n12.next = n13

print(sol.splitListToParts(head = n4, k = 3))
# Output: [[1,2,3,4],[5,6,7],[8,9,10]]