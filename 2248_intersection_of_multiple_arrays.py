'''
# TODO WIP
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
        res = set(nums[0]) # initialize result as first list
        for i in range(1, len(nums)): # loop through rest of lists in nums
            res &= set(nums[i]) # &= gets the intersection of current res and next list as a set
        res = list(res) # change into list
        res.sort() # sort into ascending order
        return res
            

sol = Solution()

print(sol.intersection(nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]])) # [3,4]

print(sol.intersection(nums = [[1,2,3],[4,5,6],[10]])) # []