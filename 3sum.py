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
        # need set to store triplets
        # will have to try all combinations
        triplets = []
        j = 1
        k = len(nums) - 1

        for i in range(len(nums)):
            # add sorted triplet to set
            # check if sorted triplet is already in list before adding
            if j <= len(nums) - 1 and nums[i] + nums[j] + nums[k] == 0:
                s_triplet =  sorted([nums[i], nums[j], nums[k]]) 
                if s_triplet not in triplets:
                    triplets.append(s_triplet)
            j = i + 2
            k -= 1
        return triplets
        


sol = Solution()

print(sol.threeSum(nums = [-1,0,1,2,-1,-4]))
# [-4, -1, -1, 0, 1, 2]

print(sol.threeSum(nums = [0,1,1]))
#[0, 1, 1]

print(sol.threeSum(nums = [0,0,0]))
# [0, 0, 0]