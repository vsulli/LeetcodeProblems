# TODO WIP
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # need to have flag turned on/off once 0 reached
        # need to store current sum of inner section
        # need to create new linked list for res

        flag = False
        sum = 0
        dummy = ListNode()
        res = dummy

        curr = head

        while curr:
            # second 0, add new node to result 
            if curr.val == 0 and flag:
                res.next = ListNode(sum)
                



sol = Solution()


n1 = ListNode(0)
n2 = ListNode(3)
n3 = ListNode(1)
n4 = ListNode(0)
n5 = ListNode(4)
n6 = ListNode(5)
n7 = ListNode(2)
n8 = ListNode(0)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8

print(sol.mergeNodes(n1))