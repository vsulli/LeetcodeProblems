''' 
Convert Binary Number in a Linked List to Integer
Leetcode # 1290
vsulli
24 July 2024

Given head which is a reference node 
to a singly-linked list. The value of 
each node in the linked list is either 
0 or 1. The linked list holds the binary 
representation of a number.

Return the decimal value of the number 
in the linked list.

The most significant bit is at the head 
of the linked list.
'''
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # "doubling" solution?
        sum = 0
        
        curr = head
        while curr:
            sum = 2 * sum + curr.val
            curr = curr.next
        
        return sum


n1 = ListNode(0)
n2 = ListNode(0)
n3 = ListNode(0)
n4 = ListNode(0)
n5 = ListNode(0)
n6 = ListNode(0)
n7 = ListNode(1)
n8 = ListNode(1)
n9 = ListNode(1)
n10 = ListNode(0)
n11 = ListNode(0)
n12 = ListNode(1)
n13 = ListNode(0)
n14 = ListNode(0)
n15 = ListNode(1)


n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n9
n9.next = n10
n10.next = n11
n11.next = n12
n12.next = n13
n13.next = n14
n14.next = n15

sol = Solution()





print(sol.getDecimalValue(n1)) # getting wrong answer for input [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]