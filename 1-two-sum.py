'''
Two Sum
Leetcode # 1
vsulli
8 June 2024

Given an array of integers nums, and an integer target
return the indices of the two numbers such that they add up to 
target
exactly one solution, can't use same element twice
can return answer in any order
'''

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        visited_dict = {}
        
        for i in range(len(nums)):
            # number you're looking for already in dict
            if target - nums[i] in visited_dict:
                return [i, visited_dict[target - nums[i]]]
            else:
                # add current num to dict
                visited_dict[nums[i]] = i
        


sol = Solution()

print(sol.twoSum([2, 7, 11, 15], target = 9))

print(sol.twoSum([3, 2, 4], target = 6))

print(sol.twoSum([3, 3], target = 6))