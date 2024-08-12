# 12 August 2024

# Review - 217 - Contains Duplicate

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


sol = Solution()
print(sol.containsDuplicate(nums = [1,2,3,1]))

print(sol.containsDuplicate(nums = [1,2,3,4]))

print(sol.containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2]))