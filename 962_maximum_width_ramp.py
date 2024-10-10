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
        # monotonic stack
        stack = [0]
        n = len(nums)
        for i in range(1, n):
            if nums[i] < nums[stack[-1]]:
                stack.append(i)
        
        res = 0
        for i in range(n - 1, -1, -1):
            while stack and  nums[i] >= nums[stack[-1]]:
                j =  stack.pop()
                res = max(res, i - j)
        return res
    

            


sol = Solution()

print(sol.maxWidthRamp(nums = [6,0,8,2,1,5])) # 4

print(sol.maxWidthRamp(nums = [9,8,1,0,1,9,4,0,4,1])) # 7

print(sol.maxWidthRamp(nums =[2,2,1])) # 1
