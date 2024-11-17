'''
Remove Duplicates from Sorted Array
Leetcode # 26
vsulli
16 June 2024

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

'''

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # loop through 
        # keep track of index
        i2 = 1
        if len(nums) == 1:
            return 1
        for i in range(len(nums)): 
            # if curr number is greater than last one, place it at index i2
            if nums[i] > nums[i-1]:
                nums[i2] = nums[i]
                i2 +=1
        return i2