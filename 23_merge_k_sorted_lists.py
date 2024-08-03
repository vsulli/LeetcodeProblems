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
        # O(nlogk) 

        if not lists or len(lists) == 0:
            return None
        
        # take pairs of linked lists and merge them
        # until only one output
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]
    
    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next

            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2: 
            tail.next = l2
        return dummy.next

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

n9 = None

print(sol.mergeKLists([n1, n4, n7]))

print(sol.mergeKLists([n9]))