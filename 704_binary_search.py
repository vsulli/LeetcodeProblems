
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
        # since list is sorted, choose middle of list
        # check if matches target
        # if lower check left, if higher check right
              pass

sol = Solution()

print(sol.search(nums = [-1,0,3,5,9,12], target = 9))

print(sol.search(nums = [-1,0,3,5,9,12], target = 2))