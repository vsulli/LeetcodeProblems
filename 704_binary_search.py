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

def searchArray(nums: List[int], guess, target):
    if len(nums) == 1 and nums[guess] != target:
        return -1
    
    elif nums[guess] == target:
        return guess
    
    elif nums[guess] < target:
        searchArray(nums, guess, target)

    elif nums[guess] > target:


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # since list is sorted, choose middle of list
        # check if matches target
        # if lower check left, if higher check right
        # if reach number that is less than target, return -1

        # initialize index to middle
        guess = len(nums) // 2

        start = 0
        end = len(nums)

        while nums[guess] != target and nums:
            # search right
            if nums[guess] < target:
                nums = splitArray(nums, guess, end)
                guess = (len(nums) - guess) // 2

            # search left
            if nums[guess] > target:
                nums = splitArray(nums, start, guess)
                guess = (len(nums) - guess) // 2
        
        if not nums:
            return -1
        
        return guess


sol = Solution()

print(sol.search(nums = [-1,0,3,5,9,12], target = 9)) # 4
'''

print(sol.search(nums = [-1,0,3,5,9,12], target = 2)) # -1

print(sol.search(nums = [1, 2, 3, 4, 5], target = 2)) #  1
'''