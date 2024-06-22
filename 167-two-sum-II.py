'''
Two Sum II - Input Array is Sorted
Leetcode # 167
vsulli
22 June 2024

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
There is exactly one solution
'''

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # no extra storing of nums and sum
        # sorted, so if sum is too low, need to increment right pointer?
        # nested for loop?
        j = 1
        for i in range(len(numbers)):
            while j < len(numbers) and numbers[i] + numbers[j] < target:
                j+=1
            if j < len(numbers) and numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            j = i + 2

sol = Solution()


print(sol.twoSum(numbers = [2,7,11,15], target = 9)) # [1, 2]


print(sol.twoSum(numbers = [2,3,4], target = 6)) # [1, 3]

print(sol.twoSum(numbers = [-1,0], target = -1)) # [1,2]


print(sol.twoSum(numbers = [5,25,75], target = 100)) # [2, 3]