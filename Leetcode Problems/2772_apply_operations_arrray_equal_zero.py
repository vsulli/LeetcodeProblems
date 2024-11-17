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
        # initialize an empty array 1 larger than nums
        arr = [0]*(len(nums)+1)
        h = 0 # least number we need so far
        for i, n in enumerate(nums): # getting index and number
            h -= arr[i]
            if n > h:
                if i+k > len(nums):
                    return False
                arr[i+k] = n-h
                h = n
            elif n < h:
                return False
        return True

sol = Solution()
print(sol.checkArray(nums = [2,2,3,1,1,0], k = 3)) # true

print(sol.checkArray(nums = [1,3,1,1], k = 2)) # false 
# not possible because jump between subarrays is greater than 1 and one of array elements is 1

print(sol.checkArray(nums = [0,0,51,67,80,98,88,75, 
                             89,83,100,70,77,82,57,100,80,69,19,17], k = 3)) # true

