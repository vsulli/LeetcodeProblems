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
        if len(nums) == 1:
            return 
        i1 = 0
        i2 = 1
        # find minimum and set up as first spot
        min_num_index = nums.index(min(nums))
        temp = nums[i1]
        nums[i1] = nums[min_num_index]
        nums[min_num_index] = temp

        # print(min_num_index)
        # print(nums)
        i1 = 1
        i2 = i1 + 1

        while i1 < i2 and i2 <= (len(nums) - 1):
            if nums[i2] < nums[i1]:
                while i2 <= len(nums) - 1 and nums[i2] < nums[i1]:
                    temp = nums[i1]
                    nums[i1] = nums[i2]
                    nums[i2] = temp
                    i2 += 1
            else:
                i1+=1
                i2 = i1 + 1
        print(nums)
        

sol = Solution()

sol.sortColors(nums = [0]) 
sol.sortColors(nums = [2,0,2,1,1,0]) # [0,0,1,1,2,2]
sol.sortColors(nums = [2,0,1]) # [0,1,2]
sol.sortColors(nums = [2,2,1,0,1,0,2]) # [0,0,1,1,2,2,2]