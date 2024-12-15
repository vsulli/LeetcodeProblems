# 167 Two Sum II - Input Array is Sorted

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 1-indexed array, sorted in non-decreasing order
        # find the two numbers that add up to targest
        # return the indices of the two numbers
        # guaranteed solution
        p1 = 0
        p2 = 1
        while numbers[p1] + numbers[p2] != target:
            # when do you increment the left pointer vs right pointer?
            sum = numbers[p1] + numbers[p2]
            if sum > target:
                p1 -= 1
            elif sum < target and p2 != len(numbers) - 1:
                p2 += 1
            elif sum < target and p2 == len(numbers) - 1:
                p1 += 1

        return [p1 + 1, p2 + 1]


sol = Solution()

print(sol.twoSum(numbers = [2,7,11,15], target = 9))

print(sol.twoSum(numbers = [2,3,4], target = 6))

print(sol.twoSum(numbers = [-1,0], target = -1))

print(sol.twoSum(numbers = [2,7,11,15], target = 18))