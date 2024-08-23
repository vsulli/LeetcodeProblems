'''
Number of Sub-arrays of Size K and Average
Greater than or Equal to Threshold
Leetcode # 209
vsulli
22 August 2024

Given an array of positive integers nums and 
a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to 
 target. If there is no such subarray, return 0 instead.

'''

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        sum = 0
        l = 0
        r = 0
        length = 0

        while r != len(nums) - 1:
            if nums[l] == target:
                return length




sol = Solution()
print(sol.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))

print(sol.minSubArrayLen(target = 4, nums = [1,4,4]))

print(sol.minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1]))