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
        # take target - numbers[i]
        # search for other number in right side of array?
        # get that index?

        for i in range(len(numbers)):
            # number you need to find
            num = target - numbers[i]
            try: 
                numbers.index(num, i+1)
                return [i+1, numbers.index(num, i+1) + 1]
            # if number does not exist in the list
            except ValueError:
                pass


sol = Solution()


print(sol.twoSum(numbers = [2,7,11,15], target = 9)) # [1, 2]


print(sol.twoSum(numbers = [2,3,4], target = 6)) # [1, 3]

print(sol.twoSum(numbers = [-1,0], target = -1)) # [1,2]


print(sol.twoSum(numbers = [5,25,75], target = 100)) # [2, 3]