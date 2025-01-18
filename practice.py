from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # start with two pointers in the middle?
        # move right if need greater, move left if need smaller?
        l = (len(numbers) // 2 ) - 1
        r = l + 1
        curr_sum = numbers[l] + numbers[r]
        while curr_sum != target:
            if curr_sum < target and r < len(numbers):
                # need to increase value
                r += 1
            elif curr_sum > target and l > len(numbers):
                l -= 1
            curr_sum = numbers[l] + numbers[r]
        return [l, r]



sol =  Solution()

print(sol.twoSum(numbers = [2,7,11,15], target = 9))

print(sol.twoSum(numbers = [2,3,4], target = 6))

print(sol.twoSum(numbers = [-1,0], target = -1))