'''
# TODO adjust to have dummy node in first position
Remove Nth Node From End of List
Leetcode # 19
vsulli
12 July 2024

Given the head of a linked list, remove the 
nth node from the end of the list and return its head.

 
'''

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def printList(head: ListNode):
    curr = head
    while curr:
            print(curr.val)
            curr = curr.next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # will have to loop through at least once to get the full size
        # size - (n-1)(node to remove)
        # if size == 1
        # return empty node?

        curr = head.next
        size = 1

        while curr:
            size += 1
            curr = curr.next
        
        if size == 1:
            return ListNode()
        
        count = 1
        curr = head
        while curr:
            count += 1
            if count == (size - (n -1)):
                curr.next = curr.next.next
            curr = curr.next

        return head
        

            

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

print(sol.removeNthFromEnd(n1, n = 1))
b1 = ListNode(1)

print(sol.removeNthFromEnd(b1, n = 1))