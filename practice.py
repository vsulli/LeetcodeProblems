# 1 Two Sum

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int)->List[int]:
        res = []
        seen = {} # num: index
        for i, n in enumerate(nums):
            if target - n in seen:
                return [seen[target - n], i]
            else:
                seen[n] = i
        return res


sol = Solution()

print(sol.twoSum(nums = [2,7,11,15], target = 9)) # [0, 1]
print(sol.twoSum(nums = [3,2,4], target = 6))