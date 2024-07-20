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
        pass

sol = Solution()

sol.sortColors(nums = [2,0,2,1,1,0]) # [0,0,1,1,2,2]
sol.sortColors(nums = [2,0,1]) # [0,1,2]