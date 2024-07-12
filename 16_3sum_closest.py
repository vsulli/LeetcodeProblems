'''
3Sum Closest
Leetcode # 16
vsulli
11 July 2024

 Given an integer array 
 nums of length n and an 
 integer target, find three 
 integers in nums such that 
 the sum is closest to target.

Return the sum of the three 
integers.

You may assume that each input 
would have exactly one solution.
'''

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        # sort nums
        # start as 2 sum
        # then iterate through remaining?
        sorted_nums = sorted(nums)
        closest_sum = None
        l = 0
        r = len(nums) - 1
        m = int(len(nums) - 1 / 2) 
        while l != r:
            current_sum = nums[l] + nums[r] + nums[m]
            if abs(target - current_sum) < abs(target - closest_sum):
                closest_sum = current_sum
            
            if current_sum > target:
                r -= 1
            elif current_sum < target:
                l += 1
        return closest_sum
            


sol = Solution()

print(sol.threeSumClosest(nums = [-1,2,1,-4], target = 1))
# 2
#[-4, -1, 1, 2]

print(sol.threeSumClosest(nums = [0,0,0], target = 1))
# 0