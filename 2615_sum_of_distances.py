''' 
Sum of Distances
Leetcode # 2615
vsulli
8 August 2024

You are given a 0-indexed integer 
array nums. There exists an array 
arr of length nums.length, where 
arr[i] is the sum of |i - j| over 
all j such that nums[j] == nums[i] 
and j != i. If there is no such j, 
set arr[i] to be 0.

Return the array arr.
 
'''
class Solution:
    def distance(self, nums: list[int]) -> list[int]:
        # answer array to return
        arr = [0] * len(nums)
        distinct = set(nums)
        distinct_indices = {} # num: indices

        # if all distinct then return array of 0s
        if len(distinct) == len(nums):
            return [0] * len(nums)

        # add all nums to dictionary with all of their indices
        for i in range(0, len(nums)):
            if nums[i] in distinct_indices:
                distinct_indices[nums[i]].append(i)
            else:
                distinct_indices[nums[i]] = [i]

        # calculate all the values for each index with lookups in dict?
        for i in range(0, len(nums)):
            # get the value at nums[i]
            # look that value up in dict
            # take the sum of all the abs diffs of the indices in that list
            values = distinct_indices.get(nums[i])
            for val in values:
                arr[i] += abs(i - val)

        return arr

sol = Solution()

print(sol.distance(nums = [1,3,1,1,2])) # [5, 0, 3, 4, 0]

print(sol.distance(nums = [0,5,3])) # [0, 0, 0]