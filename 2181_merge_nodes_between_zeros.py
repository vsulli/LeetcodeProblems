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
        # Initialize a sentinel/dummy node with the first non-zero value.
        modify = head.next
        next_sum = modify

        while next_sum:
            sum = 0
            # Find the sum of all nodes until you encounter a 0.
            while next_sum.val != 0:
                sum += next_sum.val
                next_sum = next_sum.next

            # Assign the sum to the current node's value.
            modify.val = sum
            # Move nextSum to the first non-zero value of the next block.
            next_sum = next_sum.next
            # Move modify also to this node.
            modify.next = next_sum
            modify = modify.next
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