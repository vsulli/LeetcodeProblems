# 167 Two Sum II - Input Array is Sorted

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # start on outsides
        l, r = 0, len(numbers) - 1

        while l < r:
            cur_sum = numbers[l] + numbers[r]
            if cur_sum > target:
                r -= 1
            elif cur_sum < target:
                l += 1
            else:
                return [l + 1, r + 1]


sol = Solution()

print(sol.twoSum(numbers = [2,7,11,15], target = 9)) #indices 1, 2

print(sol.twoSum(numbers = [2,3,4], target = 6)) # indices 1, 3

print(sol.twoSum(numbers = [-1,0], target = -1)) # 1, 2

print(sol.twoSum(numbers = [2,7,11,15], target = 18)) # 2, 3