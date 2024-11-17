'''
Number of Sub-arrays of Size K and Average
Greater than or Equal to Threshold
Leetcode # 209
vsulli
22 August 2024

Given an array of positive integers nums and 
a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to 
 target. If there is no such subarray, return 0 instead.

'''

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l, total = 0, 0
        res = float("inf")

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(r - l + 1, res)
                total -= nums[l]
                l += 1


        return 0 if res == float("inf") else res

            




sol = Solution()

'''

print(sol.minSubArrayLen(target = 8, nums = [7])) # 0

print(sol.minSubArrayLen(target = 8, nums = [8])) # 1


print(sol.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3])) # 2
'''

print(sol.minSubArrayLen(target = 4, nums = [1,4,4])) # 1

'''

print(sol.minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1])) # 0
'''
