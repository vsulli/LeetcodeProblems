# LC 1 - Two Sum

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            if target - nums[i] in seen:
                return [seen[target-nums[i]], i]
            seen[nums[i]] = i
    
sol = Solution()

print(sol.twoSum(nums = [2,7,11,15], target = 9))

print(sol.twoSum(nums = [3,2,4], target = 6))

print(sol.twoSum(nums = [3,3], target = 6))