'''
Find Score of an Array After Marking
All Elements
Leetcode # 2593
vsulli
13 December 2024

You are given an array nums consisting 
of positive integers.

Starting with score = 0, apply the following 
algorithm:

Choose the smallest integer of the array that 
is not marked. If there is a tie, choose the 
one with the smallest index.
Add the value of the chosen integer to score.
Mark the chosen element and its two adjacent 
elements if they exist.
Repeat until all the array elements are marked.
Return the score you get after applying the 
above algorithm.
'''
from typing import List

class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0


sol = Solution()

print(sol.findScore(nums = [2,1,3,4,5,2]))

print(sol.findScore(nums = [2,3,5,1,3,2]))