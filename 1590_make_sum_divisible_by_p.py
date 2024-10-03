'''
Make Sum Divisible by P
Leetcode # 1590
vsulli
3 October 2024

Given an array of positive integers nums, remove the 
smallest subarray (possibly empty) such that the sum of 
the remaining elements is divisible by p. It is not allowed 
to remove the whole array.

Return the length of the smallest subarray that you need to 
remove, or -1 if it's impossible.

A subarray is defined as a contiguous block of elements in 
the array.
 
'''

from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        pass

sol = Solution()

print(sol.minSubarray(nums = [3,1,4,2], p = 6))

print(sol.minSubarray(nums = [6,3,5,2], p = 9))

print(sol.minSubarray(nums = [1,2,3], p = 3))