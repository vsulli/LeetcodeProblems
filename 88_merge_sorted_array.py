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
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]




sol = Solution()
sol.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
