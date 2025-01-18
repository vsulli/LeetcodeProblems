from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers on opposite ends of list
        l, r = 0, len(numbers) - 1

        while l < r:
            curr_sum = numbers[l] + numbers[r]

            if curr_sum > target:
                r -= 1
            elif curr_sum < target:
                l += 1
            else:
                return [l + 1, r + 1] # 1-indexed array


sol =  Solution()

print(sol.twoSum(numbers = [2,7,11,15], target = 9))

print(sol.twoSum(numbers = [2,3,4], target = 6))

print(sol.twoSum(numbers = [-1,0], target = -1))