''' 
Reverse Nodes in k-Group
Leetcode # 25
vsulli
10 August 2024

Given the head of a linked list, reverse the nodes
of the list k at a time, and return the modified list

k is a positive integer and is less than or equal to the length of 
the linked list. If the number of nodes is not a multiple of k
then left-out nodes, in the end, should remain as it is

You may not alter the values in the list's nodes, only nodes
themselves may be changed
 
'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pass

sol = Solution()

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5


print(sol.reverseKGroup(head = n1, k = 2)) # [2, 1, 4, 3, 5]
# reversing two at a time