# 209 - Minimum Size Subarray Sum Practice

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currSum, l = 0, 0
        minLen = float("inf")

        for r in range(len(nums)):
            currSum += nums[r]
            while currSum >= target:
                minLen = min(r - l + 1, minLen)
                currSum -= nums[l]
                l += 1
        return 0 if minLen == float("inf") else minLen

sol = Solution()

print(sol.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3])) # 2


print(sol.minSubArrayLen(target = 4, nums = [1,4,4])) # 1


print(sol.minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1])) # 0