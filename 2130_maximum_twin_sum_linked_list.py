''' 
Maximum Twin Sum of a Linked List
Leetcode # 2130
vsulli
29 July 2024

In a linked list of size n, 
where n is even, the ith node 
(0-indexed) of the linked list 
is known as the twin of the (n-1-i)th 
node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is 
the twin of node 3, and node 1 is the 
twin of node 2. These are the only nodes 
with twins for n = 4.
The twin sum is defined as the sum of a 
node and its twin.

Given the head of a linked list with even 
length, return the maximum twin sum of the 
linked list.


'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        pass

sol = Solution()


n1 = ListNode(5)
n2 = ListNode(4)
n3 = ListNode(2)
n4 = ListNode(1)

n1.next = n2
n2.next = n3
n3.next = n4

print(sol.pairSum(n1))