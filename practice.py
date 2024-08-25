# 209 - practice review

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
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
print(sol.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3])) # 2

print(sol.minSubArrayLen(target = 4, nums = [1,4,4])) # 1

print(sol.minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1])) # 0