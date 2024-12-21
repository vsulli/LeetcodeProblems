# 238 Product of Array Except SElf

from typing import List
import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # o(n) time means that you only loop through the array once
        # can't use division operator
        # get product of array except for that index
        # calculate all multiplied, find difference for that index?
        products = [0] * len(nums)
        p = 0

        for i in range(len(nums)):
            # multiply all the numbers of product from left to right of pointer?
            products[i] = math.prod(nums[0:i]) * math.prod(nums[i+1:])
            p+= 1
        return products


sol = Solution()
print(sol.productExceptSelf(nums = [1,2,3,4]))

print(sol.productExceptSelf(nums = [-1, 1, 0, -3, 3]))