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
import heapq
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        heap = [] # min heap
        k = len(lists)

        for i in range(k):
            if lists[i]: # if a valid node
                heapq.heappush(
                    heap,
                    (lists[i].val, i, lists[i]) # smallest list val, index, head of that list
                )

        # go through all nodes in all lists in ascending order
        while heap:
            _, i, node = heapq.heappop(heap) # get index and node from heap
            curr.next  = node
            curr = curr.next
            node = node.next
            # if there is still a node, still value to push onto heap
            if node:
                heapq.heappush(
                    heap,
                    (node.val, i, node)
                )

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