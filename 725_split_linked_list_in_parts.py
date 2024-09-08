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

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from typing import List, Optional


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        pass


sol = Solution()

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)

n1.next = n2
n2.next = n3

print(sol.splitListToParts(head = n1, k = 5))
# Output: [[1],[2],[3],[],[]]

n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n7 = ListNode(7)
n8 = ListNode(8)
n9 = ListNode(9)
n10 = ListNode(10)

n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n9
n9.next = n10

print(sol.splitListToParts(head = n1, k = 3))
# Output: [[1,2,3,4],[5,6,7],[8,9,10]]