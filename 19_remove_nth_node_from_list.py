'''
Remove Nth Node From End of List
Leetcode # 19
vsulli
30 July 2024

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
        # will have to loop through at least once to get size
        # go to n-1 from end to set its next pointer to next next
        # initialize dummy node as first
        # return dummy.next

        # should be able to do in one pass if initialize dummy
        # check if next value is next is n


        dummy = ListNode(-1)
        dummy.next = head


        curr = dummy.next
        size = 0

        while curr:
            size += 1
            curr = curr.next
        
        if size == 1:
            return head.next
        

        
        count = 0
        curr = dummy
        dummy.next = head
        while curr:
            if count == (size - n):
                curr.next = curr.next.next
            curr = curr.next
            count += 1

        return dummy.next
        

            

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

new = sol.removeNthFromEnd(n1, n = 2) # 1, 2, 3, 5
printList(new)
print("---")

b1 = ListNode(1)
new = sol.removeNthFromEnd(b1, n = 1) # [] none
printList(new)
print("---")

c1 = ListNode(1)
c2 = ListNode(2)
c1.next = c2

new = sol.removeNthFromEnd(c1, n = 2) # 2
printList(new)
