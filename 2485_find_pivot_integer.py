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
import math

class Solution:
    def pivotInteger(self, n: int) -> int:
        sum = (n * (n + 1) // 2)
        pivot = int(math.sqrt(sum))
        # If pivot * pivot is equal to sum (pivot found) return pivot, else return -1
        return pivot if pivot * pivot == sum else -1

sol =  Solution()

print(sol.pivotInteger(n = 8)) # 6

print(sol.pivotInteger(n = 1)) # 1

print(sol.pivotInteger(n = 4)) # -1