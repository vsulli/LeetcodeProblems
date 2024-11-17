'''
Sort List
Leetcode # 23
vsulli
4 August 2024


Given the head of a linked list, 
return the list after sorting 
it in ascending order.
'''

from math import inf
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # merge sort Time: O(nlogn) Memory: O(logn) - recursive solution

        # base case - no head node
        if not head or not head.next:
            return head
        
        # split list into two halves
        left = head
        right = self.getMid(head)
        temp = right.next
        right.next = None
        right = temp

        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)

    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, list1, list2):
        tail = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return dummy.next

sol = Solution()

n1 = ListNode(4)
n2 = ListNode(2)
n3 = ListNode(1)
n4 = ListNode(3)

n1.next = n2
n2.next = n3
n3.next = n4


print(sol.sortList(n1)) # 1,2,3,4

n5 = ListNode(-1)
n6 = ListNode(5)
n7 = ListNode(3)
n8 = ListNode(4)
n9 = ListNode(0)

n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n9


print(sol.sortList(n5)) # -1, 0, 3, 4, 5

