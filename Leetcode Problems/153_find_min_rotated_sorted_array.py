'''
Find Minimum in Rotated Sorted Array
Leetcode # 153
vsulli
12 October 2024

Suppose an array of length n sorted in 
ascending order is rotated between 1 
and n times. For example, the array 
nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], 
a[2], ..., a[n-1]] 1 time results in the 
array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of 
unique elements, return the minimum 
element of this array.

You must write an algorithm that 
runs in O(log n) time.
'''

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # keep track of start and end
        # keep track of curr min
        # loop through while l pointer less than right
        # calculate mid, new curr min
        # if mid section is greater than pointer at end, search right, else left
        start, end = 0, len(nums) - 1

        curr_min = float("inf")

        while start < end:
            mid = start + (end - start) // 2
            curr_min = min(curr_min, nums[mid])

            # right has min
            if nums[mid] > nums[end]:
                start = mid + 1

            # left has min
            else:
                end = mid - 1

        return min(curr_min, nums[start])

        

sol = Solution()

print(sol.findMin(nums = [3,4,5,1,2])) # 1

print(sol.findMin(nums = [4,5,6,7,0,1,2])) # 0

print(sol.findMin(nums = [11,13,15,17])) # 11