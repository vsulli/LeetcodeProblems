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
        # from center, back, both are same
        # make a copy that is the reversed list?
        left = []
        right = []
        count_l = 0
        count_r = 0
        curr = head
        seen = set()
        while curr:
            if curr.val in left:
                while curr.next:
                    right.append(curr.val)
                    count_r += 1
            else:
                left.append(curr.val)
                count_l +=1
            curr = curr.next
        if count_l != count_r:
            return False

        # check all keys in reverse of left are equal to right
        for i in range(len(left),-1, -1 ):
            if left[i] != right[i]:
                return False
        return True





sol = Solution()
