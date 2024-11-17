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
import bisect
class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        res = []
        seen = {} # hashmap to store count for each number
        # if count of number in seen matches len numbers, return sorted
        for i in range(len(nums)):
            for j in range(len(min(nums, key = len))):
                if nums[i][j] in seen:
                    seen[nums[i][j]] += 1
                else:
                    seen[nums[i][j]] = 1
        for k in seen:
            if seen[k] == len(nums):
                bisect.insort(res, k)
        return res
            

sol = Solution()

print(sol.intersection(nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]])) # [3,4]

print(sol.intersection(nums = [[1,2,3],[4,5,6],[10]])) # []