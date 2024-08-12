# 12 August 2024

# Review - 1 - two sum

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i in range(len(nums)):
            if target - nums[i] in visited:
                return [i, visited[target - nums[i]]] # difficult line
            else:
                visited[nums[i]] = i # difficult line
    


sol = Solution()
print(sol.twoSum(nums = [2,7,11,15], target = 9))

print(sol.twoSum(nums = [3,2,4], target = 6))

print(sol.twoSum(nums = [3,3], target = 6))