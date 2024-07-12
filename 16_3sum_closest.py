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
        # 3 pointers
        # check if current sum is closer than stored closest sum

    
        nums.sort()
        # intialize to infinity
        closest_sum = float('inf')

        # never have to go to end of nums array due to left and right pointers
        for i in range(len(nums) -2):
            l = i + 1
            r = len(nums) - 1

            # check left and right point of index
            # loop while left less than right
            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total == target: 
                    return total
                
                # check if current total less than diff of stored sum
                if abs(total - target) < abs(closest_sum - target):
                    closest_sum = total
                
                # move left pointer right
                if total < target:
                    l += 1
                else:
                    r -= 1
                    
        return closest_sum


sol = Solution()

print(sol.threeSumClosest(nums = [-1,2,1,-4], target = 1))
# 2
#[-4, -1, 1, 2]

print(sol.threeSumClosest(nums = [0,0,0], target = 1))
# 0