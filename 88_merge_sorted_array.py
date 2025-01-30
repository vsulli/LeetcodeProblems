''' 
Merge Sorted Array
Leetcode # 88
vsulli
30 January 2025
You are given two integer 
arrays nums1 and nums2, 
sorted in non-decreasing order, 
and two integers m and n, 
representing the number of elements 
in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single 
array sorted in non-decreasing order.
'''
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # nums 1 should be sorted in-place, sort in non-decreasing order (basically ascending)
        temp = None 
        p = 0
        i = 0
        while nums2:
            while nums2[i] < nums1[p]:
                p += 1

            temp = nums1[p]
            nums1[p] = nums2[i]
            nums2[i] = temp 




sol = Solution()
sol.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
