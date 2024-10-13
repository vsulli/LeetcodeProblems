'''
Search in Rotated Sorted Array
Leetcode # 33
vsulli
13 October 2024

There is an integer array nums sorted in 
ascending order (with distinct values).

Prior to being passed to your function, 
nums is possibly rotated at an unknown 
pivot index k (1 <= k < nums.length) such 
that the resulting array is [nums[k], nums[k+1],
 ..., nums[n-1], nums[0], nums[1], ..., 
 nums[k-1]] (0-indexed). For example, 
 [0,1,2,4,5,6,7] might be rotated at pivot 
 index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible 
rotation and an integer target, return the 
index of target if it is in nums, or -1 if 
it is not in nums.

You must write an algorithm with O(log n) 
runtime complexity.
'''

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # set start and end pointers
        # calculate mid
        # if target is less than mid, start and end - search right
        # else greater than start, less than mid, greater than end - search left?

        s, e = 0, len(nums) - 1
        i = -1

        if nums[s] == target:
            return s
        elif nums[e] == target:
            return e
        
        while s < e:
            m = s + (e - s) // 2
            if nums[m] == target:
                return m
            
            # search right of m
            elif target < nums[m] and target < nums[s] and target < nums[e]:
                s = m + 1

            # search left of m
            else:
                e = m - 1

        return s if nums[s] == target else -1
        

sol = Solution()

print(sol.search(nums = [1,3], target = 3)) # 1

print(sol.search(nums = [4,5,6,7,0,1,2], target = 0)) # 4

print(sol.search(nums = [4,5,6,7,0,1,2], target = 3)) # -1

print(sol.search(nums = [1], target = 0)) # -1
