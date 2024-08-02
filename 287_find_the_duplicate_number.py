'''
Find the Duplicate Number
Leetcode # 2678
vsulli
2 August 2024

Given an array of integers nums 
containing n + 1 integers where 
each integer is in the range 
[1, n] inclusive.

There is only one repeated number 
in nums, return this repeated number.

You must solve the problem without 
modifying the array nums and uses 
only constant extra space.

'''

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        return [x for x in nums if nums.count(x) > 1][0]

        

sol = Solution()

print(sol.findDuplicate(nums = [1,3,4,2,2])) # 2

print(sol.findDuplicate(nums = [3,1,3,4,2])) # 3

print(sol.findDuplicate(nums = [3,3,3,3,3])) # 3
