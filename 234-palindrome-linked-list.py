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
        





sol = Solution()
