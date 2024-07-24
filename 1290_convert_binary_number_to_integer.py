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
        # loop all the way through to create an integer?
        # start from right-most digit
        # take 2 ^ exp * digit
        # add to sum
        num = ""
        sum = 0
        exp = 0

        curr = head
        while curr:
            num = str(curr.val) + num
            curr = curr.next
        
        # loop through string backwards
        for i in range(len(num)-1, -1, -1):
            sum += (2 ** exp) * int(num[i])
            exp += 1
            
        
        return sum


n1 = ListNode(1)
n2 = ListNode(0)
n3 = ListNode(1)

n1.next = n2
n2.next = n3

sol = Solution()



print(sol.getDecimalValue(n1))

print(sol.getDecimalValue(n1)) # getting wrong answer for input [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]