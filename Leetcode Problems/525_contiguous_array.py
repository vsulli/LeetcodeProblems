'''
Contiguous Array
Leetcode # 525
vsulli
24 August 2024

Given a binary array nums, return the 
maximum length of a contiguous subarray 
with an equal number of 0 and 1.

'''


class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        zero, one = 0, 0
        res = 0

        diff_index = {} # count[1] - count[0] -> index

        for i, n in enumerate(nums):
            if n == 0:
                zero += 1
            else:
                one += 1

            if one - zero not in diff_index:
                diff_index[one - zero] = i
        
            if one == zero:
                res = one + zero
            else:
                idx = diff_index[one - zero]
                res = max(res, i - idx)

        return res

sol = Solution()

print(sol.findMaxLength(nums = [0,1])) # 2

print(sol.findMaxLength(nums = [0,1,0])) # 2

print(sol.findMaxLength(nums = [0,1,1,1,1,0])) # 2

print(sol.findMaxLength(nums = [0, 1, 0, 1])) # 4

print(sol.findMaxLength(nums = [0,0,1,0,0,0,1,1])) # 6
# 1,0,0,0,1,1
