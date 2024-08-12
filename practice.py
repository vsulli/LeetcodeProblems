# 12 August 2024

# Review - 1929 - Concatenation of Array

from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2

sol = Solution()

print(sol.getConcatenation(nums = [1, 2, 1]))
print(sol.getConcatenation(nums = [1, 3, 2, 1]))