'''
Copy List with Random Pointer
Leetcode # 2678
vsulli
1 August 2024

A linked list of length n is given 
such that each node contains an additional 
random pointer, which could point to any node 
in the list, or null.

Construct a deep copy of the list. The deep 
copy should consist of exactly n brand new nodes, 
where each new node has its value set to the value of 
its corresponding original node. Both the next and random 
pointer of the new nodes should point to new nodes in the 
copied list such that the pointers in the original list and 
copied list represent the same list state. None of the pointers 
in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original 
list, where X.random --> Y, then for the corresponding two 
nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

'''


from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        random_index = [] # store the reference to node
        dummy = Node(-1)
        head2 = dummy

        curr = head
        while curr:
            # add node values to new linked list
            head2.next = Node(curr.val)
            random_index.append([curr.random, head2.next]) # append random(to get index) and append new linked list pointer
            head2 = head2.next
            # increment original list
            curr = curr.next


        # iterate through new list
        # update their random value to pointer from list
        # to insert correct pointer reference, for each index, search list
        curr = dummy.next
        i = 0
        while curr:
            
            index = random_index[i][0]
            if index == None:
                curr.random = None
            else:
                curr.random = random_index[index][1]
            
            i += 1
            curr = curr.next

        return dummy.next

sol = Solution()

# first create nodes
n1 = Node(7)
n2 = Node(13)
n3 = Node(11)
n4 = Node(10)
n5 = Node(1)

# update their next
# update their random pointer
n1.next = n2
n1.random = None

n2.next = n3
n2.random = 0

n3.next = n4
n3.random = 4

n4.next = n5
n4.random = 2

n5.random = 0

print(sol.copyRandomList(n1))