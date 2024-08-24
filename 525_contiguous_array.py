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
        # will need to keep count of both 1s and 0s with the increase/shrinking of sliding window
        l, res = 0, 0
        count = {0: 0, 1: 0} # initialize count for each num to 0

        for r in range(len(nums)):
            count[nums[r]] += 1
            # length of sliding has to be even 
            if (r - l + 1) % 2 == 0:
                if count[0] == count[1]:
                    res = max(res, r - l + 1)
                    # if too many of either need to increase left pointer until back in balance
                    l += 1

        return res

sol = Solution()

print(sol.findMaxLength(nums = [0,1])) # 2

print(sol.findMaxLength(nums = [0,1,0])) # 2

print(sol.findMaxLength(nums = [0,1,1,1,1,0])) # 2

print(sol.findMaxLength(nums = [0, 1, 0, 1])) # 4

