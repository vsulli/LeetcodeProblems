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
        N = len(nums)

        current = 0
        delta = [0] * (N + 1)

        for i in range(N):
            current += delta[i]
            if nums[i] == current:
                continue
            if nums[i] > current:
                change = nums[i] - current
                current += change
                if i + k <= N:
                    delta[i + k] -= change
                else:
                    return False
            else:
                return False
        return True

sol = Solution()
print(sol.checkArray(nums = [2,2,3,1,1,0], k = 3)) # true

print(sol.checkArray(nums = [1,3,1,1], k = 2)) # false 
# not possible because jump between subarrays is greater than 1 and one of array elements is 1

print(sol.checkArray(nums = [0,0,51,67,80,98,88,75, 
                             89,83,100,70,77,82,57,100,80,69,19,17], k = 3)) # true

