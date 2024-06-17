'''
Remove Element
Leetcode # 27
vsulli
16 June 2024

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

'''

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i2 = 0
        for i in range(0, len(nums)): 
            # if curr num does not equal val, replace i2 with curr num
            if nums[i] != val:
                nums[i2] = nums[i]
                i2 +=1
        return i2