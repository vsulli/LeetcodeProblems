'''
Sort List
Leetcode # 23
vsulli
4 August 2024


Given the head of a linked list, 
return the list after sorting 
it in ascending order.
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertNode(self, node:ListNode, head:ListNode)-> ListNode:
        # take value of node to insert
        # search through list until you get to spot it needs to be inserted in
        # return head to list

        dummy = head
        curr = head
        while curr:
            if curr.val == None or node.val <= curr.next.val:
                temp = curr.next
                curr.next = node
                curr = curr.next
                curr.next = temp
            else:
                curr = curr.next

        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # how to reorder?
        # need a temp variable
        # need to search for absolute smallest first?
        new_list = ListNode(None)
        curr = head
        while curr:
            new_list = self.insertNode(curr, new_list)
            curr = curr.next

        return new_list



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

