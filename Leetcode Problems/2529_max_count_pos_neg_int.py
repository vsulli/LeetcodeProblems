
'''
Maximum Count of Positive Integer and Negative Integer
Leetcode #2529
vsulli
20 October 2024

Given an array nums sorted in non-decreasing order, 
return the maximum between the number of positive 
integers and the number of negative integers.

In other words, if the number of positive integers 
in nums is pos and the number of negative integers 
is neg, then return the maximum of pos and neg.
Note that 0 is neither positive nor negative.
'''

from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg=0
        pos=0
        for i in nums:
            if i>0:
                pos+=1
            if i<0:
                neg+=1

        return pos if pos > neg else neg

sol = Solution()

print(sol.maximumCount(nums = [-2,-1,-1,1,2,3])) # 3

print(sol.maximumCount(nums = [-3,-2,-1,0,0,1,2])) # 3

print(sol.maximumCount(nums = [5,20,66,1314])) # 4