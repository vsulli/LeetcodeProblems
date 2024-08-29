'''
Apply Operations to Make All Array Elements 
Equal to Zero
Leetcode # 2772
vsulli
29 August 2024

You are given a 0-indexed integer 
array nums and a positive integer k.

You can apply the following operation 
on the array any number of times:

Choose any subarray of size k from the 
array and decrease all its elements by 1.
Return true if you can make all the array 
elements equal to 0, or false otherwise.

A subarray is a contiguous non-empty part 
of an array.
'''

from typing import List


class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        # have to select a contiguous subarray of size k
        # want them to be of value 1 minimum so that when you decrease it's not negative
        # select next subarray of size 3 
            # how to determine start of subarray?
            # want subarray to end on rightmost section?
        
        makeZero = True
        p = 0 # pointer for start of subarray
        while sum(nums) != 0:
            for n in range(k):
                nums[p+n] -=1 
        # need to figure out how to adjust pointer
        # cases where you wouldn't be able to make array 0
            # size of array not divisible by k

        return makeZero

sol = Solution()
print(sol.checkArray(nums = [2,2,3,1,1,0], k = 3)) # true

print(sol.checkArray(nums = [1,3,1,1], k = 2)) # false 
# not possible because jump between subarrays is greater than 1 and one of array elements is 1