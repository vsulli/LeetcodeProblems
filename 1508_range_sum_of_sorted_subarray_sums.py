'''
Range Sum of Sorted Subarray Sums
Leetcode # 1508
vsulli
4 August 2024

You are given the array nums consisting 
of n positive integers. You computed 
the sum of all non-empty continuous 
subarrays from the array and then sorted 
them in non-decreasing order, creating a 
new array of n * (n + 1) / 2 numbers.

Return the sum of the numbers from index 
left to index right (indexed from 1), 
inclusive, in the new array. Since the 
answer can be a huge number return it 
modulo 109 + 7.
'''

class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        subarray_sums = []
        for i in range(0, len(nums)):
            subarray_sums.append(nums[i])
            for j in range(i, len(nums)-1):
                subarray_sums.append(nums[j]+nums[j+1])

        print(sorted(subarray_sums))

sol = Solution()

print(sol.rangeSum(nums = [1,2,3,4], n = 4, left = 1, right = 5)) # 13

print(sol.rangeSum(nums = [1,2,3,4], n = 4, left = 3, right = 4)) # 6

print(sol.rangeSum(nums = [1,2,3,4], n = 4, left = 1, right = 10)) # 50