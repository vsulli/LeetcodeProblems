# TODO WIP
# Definition for singly-linked list.
from typing import Optional



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def printList(self, head: ListNode):

        curr = head
        while curr:
            print(curr.val) 
            curr = curr.next

    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # BASE CASE -> if we have a single zero, simply return null
        if not head.next:
            return None
        
        # fetch sum from current 0 to next 0
        ptr = head.next
        sum = 0
        while ptr.val != 0:
            sum += ptr.val
            ptr = ptr.next
        
        # assign sum on the first node between nodes having value 0
        head.next.val = sum
        
        # call and get the answer and connect the answer to next of head->next
        head.next.next = self.mergeNodes(ptr)
        
        # return head->next..=> new head
        return head.next




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

n8 = sol.mergeNodes(n1)
sol.printList(n8)