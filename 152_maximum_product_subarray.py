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
        # find and store the max product and min product up to the point of an index
        # iterate starting at second index
        # time complexity O(n) iterate once through the array
        # space complexity O(1) only store a few variables

        max_product = min_product = global_max = nums[0]

        for i in range(1, len(nums)):
            current = nums[i]
            temp_max = max(current, current * max_product, current * min_product)
            min_product = min(current, current* max_product, current * min_product)
            max_product = temp_max
            global_max = max(global_max, max_product)
        return global_max



sol = Solution()

print(sol.maxProduct(nums = [2,3,-2,4])) # 6

print(sol.maxProduct(nums = [-2,0,-1])) # 0

print(sol.maxProduct(nums = [-4, -3])) # 12

print(sol.maxProduct(nums = [0,2])) # 2

print(sol.maxProduct(nums = [0,2,3,-1])) # 6