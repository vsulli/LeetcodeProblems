
'''
Merge Two Sorted Lists
Leetcode # 21
vsulli
14 July 2024

You are given the heads of two sorted linked lists
list1 and list2

Merge the two lists into one sorted list. The list
should be made by splicing together the nodes of the 
first two lists

Return the head of the merged linked list
'''

# Definition for singly-linked list.
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # set pointers to beginning of both lists
        # compare those nodes
        # if same, take list1 first, then add list2, increment
        # else take lower
            # increment that list
        # keep going until both are None

        head = ListNode() # make dummy node for head of list

        # first node of each list
        tempA = list1
        tempB = list2

        # 1st list less than 2nd
        if tempA.val < tempB.val:
            curr =tempA

        elif tempB.val < tempA.val:
            curr = tempB

        else:
            curr = tempB
            head.next = curr
            while curr:
                if curr.val == tempB.val:
                    temp = curr.next
                    curr.next = tempB 
                    while curr.next.val < temp.next.val:
                        curr = curr.next
                temp2 = curr.next
                curr.next = temp

        '''
        while tempA:
            print(tempA.val)
            tempA = tempA.next
        '''


        return head.next 
        


sol = Solution()

a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(4)

b1 = ListNode(1)
b2 = ListNode(3)
b3 = ListNode(4)

a1.next = a2
a2.next = a3

b1.next = b2
b2.next = b3

sol.mergeTwoLists(a1, b1)
