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
        # list is even
        # a twin of a node is (n - 1 -i)
        # need to split the list in half
        # loop through second half backwards
        # store the sums going through first and second half

        max_twin_sum = 0

        # find second half
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next # increment 2
            slow = slow.next # increment 1
        
        second = slow.next

        # reverse second half
        prev = slow.next = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # get sum from both first and second half
        first, second = head, prev

        while second:
            max_twin_sum = max(max_twin_sum, first.val + second.val)
            first = first.next
            second = second.next


        return max_twin_sum


sol = Solution()


n1 = ListNode(5)
n2 = ListNode(4)
n3 = ListNode(2)
n4 = ListNode(1)

n1.next = n2
n2.next = n3
n3.next = n4

print(sol.pairSum(n1))