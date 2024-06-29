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

        l_sum = 0
        r_sum = 0
        for i in range(len(nums)):
            if i == 0:
                if sum(nums[i+1:]) == 0:
                    return 0
            elif i == len(nums) - 1:
                if sum(nums[0:i]) == 0:
                    return 0
            else:
                nums[i-1] = l_sum + nums[i-1]
                if nums[i-1] == sum(nums[i+1:]):
                    return i
                print(nums[i-1])
        return -1


        # get prefix sum?

            
sol = Solution()
print(sol.pivotIndex(nums = [1,7,3,6,5,6])) # 3

'''

print(sol.pivotIndex(nums = [1,2,3])) # -1

print(sol.pivotIndex(nums = [2,1,-1])) # 0

'''