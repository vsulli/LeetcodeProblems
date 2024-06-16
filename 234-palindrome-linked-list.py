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

    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # only need second half of list to be reversed
        # two pointers, fast and slow
        # when fast pointer meets end, slow will be at middle
        # reverse list from that point and check if each node 
        # is equal
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        rev = self.reverse(slow)
        while rev:
            if head.val != rev.val:
                return False
            head = head.next
            rev = rev.next
        return True



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