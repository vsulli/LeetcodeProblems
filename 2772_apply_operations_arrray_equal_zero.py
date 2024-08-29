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
        pass

sol = Solution()
print(sol.checkArray(nums = [2,2,3,1,1,0], k = 3))

print(sol.checkArray(nums = [1,3,1,1], k = 2))