'''
Merge k Sorted Lists
Leetcode # 23
vsulli
3 August 2024

You are given an array of k linked-lists lists, 
each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted 
linked-list and return it.

'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        pass

sol = Solution()

n1 = ListNode(1)
n2 = ListNode(4)
n3 = ListNode(5)

n1.next = n2
n2.next = n3

n4 = ListNode(1)
n5 = ListNode(3)
n6 = ListNode(4)
n4.next = n5
n5.next = n6

n7 = ListNode(2)
n8 = ListNode(6)
n7.next = n8



print(sol.mergeKLists([n1, n4, n7]))