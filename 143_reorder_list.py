'''
Reorder List
Leetcode # 143
vsulli
28 July 2024

You are given the head of a singly linked list. 
l0 -> l1 -> ... -> ln -1 -> ln

Reorder the list to be on the following form:
l0 -> ln->l1->ln-1...

You may not modify the values in the list's nodes, only the 
nodes themselves may be changed
'''



from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None

        while second: 
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp


        # merge two halves
        first, second = head, prev
        # second half could be shorter than first half
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1

            first, second = tmp1, tmp2



                    
            



        return head
        
sol = Solution()

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)

n1.next = n2
n2.next = n3
n3.next = n4

print(sol.reorderList(n1))
