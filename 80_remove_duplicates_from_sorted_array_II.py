'''
Remove Duplicates from Sorted Array II
Leetcode # 80
vsulli
26 June 2024

Given an integer array nums sorted in non-decreasing order, 
remove some duplicates in-place such that each unique 
element appears at most twice. The relative order of 
the elements should be kept the same.

Since it is impossible to change the length of the 
array in some languages, you must instead have the 
result be placed in the first part of the array nums. 
More formally, if there are k elements after removing 
the duplicates, then the first k elements of nums should 
hold the final result. It does not matter what you leave
 beyond the first k elements.

Return k after placing the final result in the first k 
slots of nums.

Do not allocate extra space for another array. 
You must do this by modifying the input array in-place 
with O(1) extra memory.
'''

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        # each number can appear at most 2x
        # need a variable for count
        # need a variable for 2nd index

        i2 = 0
        count = 1
        i = 1
        
        while i < len(nums) - 1:
            # loop through getting count
            # same number
                # if count is two
                # else
            # not same as last number
                # just increment i
                    
        return nums
            




sol = Solution()

print(sol.removeDuplicates(nums = [1,1,1,2,2,3]))
# 5, nums = [1,1,2,2,3,_]

print(sol.removeDuplicates(nums = [0,0,1,1,1,1,2,3,3]))
# 7, nums = [0,0,1,1,2,3,3,_,_]
