'''
Maximum Width Ramp
Leetcode # 962
vsulli
10 October 2024


A ramp in an integer array nums is a pair (i, j) 
for which i < j and nums[i] <= nums[j]. The width 
of such a ramp is j - i.

Given an integer array nums, return the maximum width 
of a ramp in nums. If there is no ramp in nums, return 0.
'''

from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # two pointer
        # advance second pointer as long as second num >= first
        # once no longer true, get length j - i
        # keep track of max len 
        pass

sol = Solution()

print(sol.maxWidthRamp(nums = [6,0,8,2,1,5]))

print(sol.maxWidthRamp(nums = [9,8,1,0,1,9,4,0,4,1]))

