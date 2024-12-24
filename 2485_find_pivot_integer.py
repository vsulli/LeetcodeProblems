'''
Find the Pivot Integer
Leetcode # 2357
vsulli
23 December 2024

Given a positive integer n, find the 
pivot integer x such that:

The sum of all elements between 1 
and x inclusively equals the sum of 
all elements between x and n inclusively.
Return the pivot integer x. If no such 
integer exists, return -1. It is guaranteed 
that there will be at most one pivot index 
for the given input.

'''

class Solution:
    def pivotInteger(self, n: int) -> int:
        # pivot integer is the number from 1 -> pivot = pivot -> n
        # pivot integer may not exist so return -1

        for i in range(1, n+1):
            if sum(range(1, i+1)) == sum(range(i, n+1)):
                return i
        return -1

sol =  Solution()

print(sol.pivotInteger(n = 8)) # 6

print(sol.pivotInteger(n = 1)) # 1

print(sol.pivotInteger(n = 4)) # -1