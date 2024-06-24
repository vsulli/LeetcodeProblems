'''
Product of Array Except Self
Leetcode # 238
vsulli
13 June 2024

Given an integer array nums, return an 
array answer such that answer[i] is
equal to the product of all the elments of 
nums except nums[i]

the product of any prefix or suffix of nums is 
guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time
and without using the division operation
'''

class Solution:
    def productExceptSelf(self, nums: list[int])->list[int]:
        # calculate prefix and postfix products
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

            

sol = Solution()

print(sol.productExceptSelf(nums = [1, 2, 3, 4])) # [24,12,8,6]

print(sol.productExceptSelf(nums = [-1, 1, 0, -3, 3])) #  [0,0,9,0,0]