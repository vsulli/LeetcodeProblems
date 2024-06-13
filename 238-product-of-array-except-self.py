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
        prefix = []
        postfix = []

        product = 1
        for i in range(len(nums)):
            product*=nums[i]
            prefix.append(product)
        product = 1
        for i in range(len(nums)-1, -1, -1):
            product*=nums[i]
            postfix.append(product)

        # how to get products except that index?
        product_except_self = []
        for i in range(len(nums)):
            product_except_self[i] = prefix[i-1] * postfix[i+1]
            # product - take everything from left of that index * everything to right of that index backwards


        print(prefix)
        print(postfix)
        pass

sol = Solution()

print(sol.productExceptSelf(nums = [1, 2, 3, 4])) # [24,12,8,6]

print(sol.productExceptSelf(nums = [-1, 1, 0, -3, 3])) #  [0,0,9,0,0]