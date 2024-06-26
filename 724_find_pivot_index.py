'''
Find Pivot Index
Leetcode # 724
vsulli
28 June 2024

Given an array of integers nums, 
calculate the pivot index of this array.

The pivot index is the index where 
the sum of all the numbers strictly 
to the left of the index is equal to 
the sum of all the numbers strictly 
to the index's right.

If the index is on the left edge of 
the array, then the left sum is 0 because 
there are no elements to the left. This 
also applies to the right edge of the array.

Return the leftmost pivot index. If no 
such index exists, return -1.
'''

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)

        l_sum = 0
        for i in range(len(nums)):
            r_sum = total - nums[i] -l_sum
            if l_sum == r_sum:
                return i
            l_sum += nums[i]
        return -1

            
sol = Solution()
print(sol.pivotIndex(nums = [1,7,3,6,5,6])) # 3

print(sol.pivotIndex(nums = [1,2,3])) # -1

print(sol.pivotIndex(nums = [2,1,-1])) # 0

