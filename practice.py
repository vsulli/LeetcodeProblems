# leetcode 704 - binary search
# Binary Search

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left and right pointer
        # initialize middle 
        # while l < r
        # if m > target, set right == middle
        # if m < target, set left == middle
        # if it equals target, return it
        # otherwise return -1

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1

sol = Solution()

print(sol.search(nums = [-1,0,3,5,9,12], target = 9)) # 4

print(sol.search(nums = [-1,0,3,5,9,12], target = 2)) # -1