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
        # try sum of entire array
        # if isn't greater or equal return 0
        # if it is greater shrink from right while still greater than equal
        # shrink from left otherwise?

        sumNums = sum(nums)
        if sumNums < target:
            return 0
        indices = [0, len(nums)-1]
        while sumNums >= target:
            # subtract from right
            if sumNums - nums[indices[1]] >= target:
                indices[1] -= 1
            




sol = Solution()
print(sol.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))

print(sol.minSubArrayLen(target = 4, nums = [1,4,4]))

print(sol.minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1]))