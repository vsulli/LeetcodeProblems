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
        if len(nums) == 1 and sumNums == target:
            return 1
        
        indices = [0, 1]
        sumNums = sum(nums[:1])
        while sumNums < target:
            # add to right
            while sumNums < target:
                indices[1] += 1
                sumNums = sum(nums[indices[0]:indices[1]])
        
        return indices[1] - indices[0]
            




sol = Solution()

print(sol.minSubArrayLen(target = 8, nums = [7])) # 0

print(sol.minSubArrayLen(target = 8, nums = [8])) # 1


print(sol.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3])) # 2

print(sol.minSubArrayLen(target = 4, nums = [1,4,4])) # 1

print(sol.minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1])) # 0
