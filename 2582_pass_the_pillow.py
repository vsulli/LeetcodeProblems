'''
Pass the Pillow
Leetcode # 2582
vsulli
5 July 2024

There are n people standing in a line 
labeled from 1 to n. The first person 
in the line is holding a pillow initially. 
Every second, the person holding the pillow 
passes it to the next person standing in the 
line. Once the pillow reaches the end of the 
line, the direction changes, and people 
continue passing the pillow in the opposite 
direction.

For example, once the pillow reaches the 
nth person they pass it to the n - 1th 
person, then to the n - 2th person and 
so on.
Given the two positive integers n and 
time, return the index of the person 
holding the pillow after time seconds.

'''
class Node:
    def __init__(self, val: int, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next


class LinkedList:
    pass

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        length = n - 1
        index = 0
        direction = "r"
        # while loop
        # while time not up, increment i
        n = 1
        while time != 0:
            if index == length:
                direction = 'l'
            if index == 0:
                direction = 'r'
            # if not at end of array increment right
            if direction == 'r':
                index += 1
                n += 1
            # else increment left
            else:
                index -=1
                n -= 1
            time -= 1
        return n

sol = Solution()

print(sol.passThePillow(n = 4, time = 5))

print(sol.passThePillow(n = 3, time = 2))