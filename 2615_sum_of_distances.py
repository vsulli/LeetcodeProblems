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
from collections import defaultdict


class Solution:
    def distance(self, nums: list[int]) -> list[int]:
        # prefix sum
        # get sum from left and right
        res = [0] * len(nums)
        
        #hashmap to track sum
        sum_left = defaultdict(int)
        cnt_left = defaultdict(int)

        for i, x in enumerate(nums):
            res[i] +=  cnt_left[x] * i 
            res[i] -= sum_left[x] 

            cnt_left[x] += 1
            sum_left[x] += i
        
        sum_right = defaultdict(int)
        cnt_right = defaultdict(int)

        for i, x in reversed(list(enumerate(nums))):
            res[i] += sum_right[x]
            res[i] -= cnt_right[x] * i

            cnt_right[x] += 1
            sum_right[x] += i

        return res

sol = Solution()

print(sol.distance(nums = [1,3,1,1,2])) # [5, 0, 3, 4, 0]

print(sol.distance(nums = [0,5,3])) # [0, 0, 0]