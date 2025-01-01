
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # num: index
        for i in range(len(nums)):
            if target-nums[i] in seen:
                return [seen[target-nums[i]], i]
            else:
                seen[nums[i]] = i


sol = Solution()

print(sol.twoSum(nums = [2,7,11,15], target = 9)) # [0, 1]

print(sol.twoSum(nums = [3,2,4], target = 6)) # [1,2]

print(sol.twoSum(nums = [3,3], target = 6)) # [0, 1]