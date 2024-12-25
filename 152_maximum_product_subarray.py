'''
Maximum Product Subarray
Leetcode # 152
vsulli
25 December 2024

Given an integer array nums, find a subarray that
has the largest product, and return the product.

The test cases are generated so that the answer will fit
in a 32-bit integer.

'''
from typing import List

import math
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best_product = nums[0]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                curr_product = math.prod(nums[i:j+1])
                best_product = max(curr_product, best_product)

        return best_product



sol = Solution()

print(sol.maxProduct(nums = [2,3,-2,4])) # 6

print(sol.maxProduct(nums = [-2,0,-1])) # 0

print(sol.maxProduct(nums = [-4, -3])) # 12