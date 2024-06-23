'''
3Sum
Leetcode # 167
vsulli
23 June 2024

Given an integer array nums, return all the triplets
nums[i], nums[j], nums[k]
such that i != j, i != k, and j != k and their sum equals 0

no duplicates
'''

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # need three pointers?
        # left, right, mid?
        # sort array first?
        l, l2, r = 0, 1, len(nums) - 1

        while l < l2 < r:
            if nums[l] + nums[l2] + nums[r] == 0:
                return [nums[l], nums[l2], nums[r]]
            elif nums[l] + nums[l2] + nums[r] < 0:
                l +=1
            elif nums[l] + nums[l2] + nums[r] > 0:
                r -= 1
        


sol = Solution()

print(sol.threeSum(nums = [-1,0,1,2,-1,-4]))
# [-4, -1, -1, 0, 1, 2]

print(sol.threeSum(nums = [0,1,1]))
#[0, 1, 1]

print(sol.threeSum(nums = [0,0,0]))
# [0, 0, 0]