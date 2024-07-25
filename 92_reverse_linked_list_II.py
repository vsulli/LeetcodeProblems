''' 
Reverse Linked List II
Leetcode # 92
vsulli
24 July 2024

Given the head of a singly linked 
list and two integers left and 
right where left <= right, reverse 
the nodes of the list from position 
left to position right, and return 
the reversed list.
'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        n = 1
        if left == right:
            return head
        
        reverse_section = []

        rev_res = ListNode()
        res = rev_res

        curr = head
        while curr:

            # beginning of reverse section
            if n == left:
                while n != right:
                    reverse_section.append(curr.val)
                    n += 1
                    curr = curr.next
                reverse_section.append(curr.val)
                curr = curr.next
                n += 1
                 # end of reverse section
                print(reverse_section)
                for i in range(len(reverse_section)-1, -1, -1):
                    res.next = ListNode(reverse_section[i])
                    res = res.next

            # adding next node
            else:
                res.next = ListNode(curr.val)
                res = res.next
                curr = curr.next
                n += 1

        return rev_res.next



sol = Solution()

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n6 = ListNode(5)

n7 = ListNode(3)
n8 = ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

n7.next = n8

print(sol.reverseBetween(head = n1, left = 2, right = 4)) # [1,4,3,2,5]

print(sol.reverseBetween(head = n6, left = 1, right = 1)) # [5]

print(sol.reverseBetween(head = n7, left = 1, right = 2)) # [5, 3]