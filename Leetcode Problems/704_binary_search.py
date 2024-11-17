# TODO read up on recursion and binary search
'''
Binary Search
Leetcode # 704
vsulli
10 September 2024

Given an array of integers nums which 
is sorted in ascending order, and an 
integer target, write a function to search 
target in nums. If target exists, then return 
its index. Otherwise, return -1.

You must write an algorithm with O(log n) 
runtime complexity.
'''

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # don't need to actually update nums, just pointers
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
'''

print(sol.search(nums = [-1,0,3,5,9,12], target = 2)) # -1

print(sol.search(nums = [1, 2, 3, 4, 5], target = 2)) #  1
'''