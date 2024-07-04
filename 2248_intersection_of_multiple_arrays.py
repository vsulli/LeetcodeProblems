'''
Intersection of Multiple Arrays
Leetcode # 2248
vsulli
4 July 2024

Given a 2D integer array nums where nums[i] is a 
non-empty array of distinct positive integers, 
return the list of integers that are present in 
each array of nums sorted in ascending order.
'''

class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        res = []
        # sort lists
        # loop through all lists in order
        # if n in both then add to array
        # arrays don't have to be the same length
        for i,n in enumerate(min(nums)):
            

sol = Solution()

print(sol.intersection(nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]])) # [3,4]

print(sol.intersection(nums = [[1,2,3],[4,5,6]])) # []