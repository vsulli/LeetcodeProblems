# TODO figure out algorithm that uses less memory
'''
Palindrome Linked List
Leetcode # 234
vsulli
15 June 2024

Given the head of a singly linked list,
return rue if it is a palindrome or false otherwise
'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # loop through once to get length of linked list
        # go through until halfway and then reverse linked list
        # from there and check with two pointers if they're the same
        seen_list = []
        isPalindrome = True
        length = 0

        curr = head
        curr2 = ListNode(head.val)
        while curr:
            length +=1
            curr = curr.next
        if length == 1:
            return True
        curr = head
        for i in range(length // 2):
            seen_list.append(curr.val)
            print(curr.val)
            # get to half way point
            curr = curr.next
        i = len(seen_list) - 1
        if length % 2 != 0:
            curr = curr.next
        while curr:
            if seen_list[i] != curr.val:
        
                return False
            i -= 1
            curr = curr.next

        return isPalindrome



l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(2)
l4 = ListNode(1)

l5 = ListNode(1)
l6 = ListNode(0)
l7 = ListNode(1)

l1.next = l2
l2.next = l3
l3.next = l4

l5.next = l6
l6.next = l7
sol = Solution()
print(sol.isPalindrome(l1))

print(sol.isPalindrome(l5))