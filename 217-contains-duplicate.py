'''
Contains Duplicate
Leetcode # 217
vsulli
10 June 2024

Given an integer array nums, return true
if any value appears at least twice in the array,
and return false if every element is distinct. 
'''

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))

sol = Solution()
print(sol.containsDuplicate(nums = [1,2,3,1])) # true

print(sol.containsDuplicate(nums = [1,2,3,4])) # false

print(sol.containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2])) # true