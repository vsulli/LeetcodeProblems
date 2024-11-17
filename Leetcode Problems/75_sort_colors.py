''' 
Sort Colors
Leetcode # 75
vsulli
20 July 2024

Given an array nums with n objects colored 
red, white, or blue, sort them in-place 
so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to 
represent the color red, white, and blue, respectively.

You must solve this problem without using
 the library's sort function.
'''

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        # count the number of occurrences for each number
        # set indices for count length to each number
        zeroes, ones, n = 0, 0, len(nums)

        for num in nums:
            if num == 0:
                zeroes += 1
            elif num == 1:
                ones += 1
            # don't have to keep track of 2's

        for i in range(0, zeroes):
            nums[i] = 0
        for i in range(zeroes, zeroes + ones):
            nums[i] = 1

        for i in range(zeroes + ones, n):
            nums[i] = 2
        

sol = Solution()

sol.sortColors(nums = [0]) 
sol.sortColors(nums = [2,0,2,1,1,0]) # [0,0,1,1,2,2]
sol.sortColors(nums = [2,0,1]) # [0,1,2]
sol.sortColors(nums = [2,2,1,0,1,0,2]) # [0,0,1,1,2,2,2]