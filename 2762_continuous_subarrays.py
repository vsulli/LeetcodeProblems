'''  # TODO
Continuous Subarrays
Leetcode # 2762
vsulli
14 December 2024

You are given a 0-indexed integer array nums. A subarray of nums is called continuous if:

Let i, i + 1, ..., j be the indices in the subarray. Then, for each pair of indices i <= i1, i2 <= j, 0 <= |nums[i1] - nums[i2]| <= 2.
Return the total number of continuous subarrays.

A subarray is a contiguous non-empty sequence of elements within a
'''
from typing import List

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        subarray_count = 0
        # should be able to calculate with just math?
        # length of the original
        max = set()
        while len(nums[0]) != len(nums):
            pass

        

sol = Solution()

print(sol.continuousSubarrays(nums = [5,4,2,4]))

print(sol.continuousSubarrays(nums = [1,2,3]))