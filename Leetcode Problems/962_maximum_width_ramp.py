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
        # neetcode solution
        # pre-processing - get max value by going through array from right
        max_right = [0] * len(nums)

        i = len(nums) - 1
        prev_max = 0
        for n in reversed(nums):
            max_right[i] = max(n, prev_max)
            prev_max = max_right[i]
            i -= 1
        
        res = 0
        l = 0
        for r in range(len(nums)):
            while nums[l] > max_right[r]:
                l += 1

            res = max(res, r - l)
        return res

            


sol = Solution()

print(sol.maxWidthRamp(nums = [6,0,8,2,1,5])) # 4

print(sol.maxWidthRamp(nums = [9,8,1,0,1,9,4,0,4,1])) # 7

print(sol.maxWidthRamp(nums =[2,2,1])) # 1
