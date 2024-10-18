
'''
Median of Two Sorted Arrays
Leetcode #4
vsulli
18 October 2024

Given two sorted arrays nums1 and 
nums2 of size m and n respectively, 
return the median of the two sorted 
arrays.

The overall run time complexity 
should be O(log (m+n)).
 
'''

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # need to merge array first?
        # or use pointers in both lists?

        l1, r1 = 0, 0
        l2, r2 = len(nums1) - 1, len(nums2) - 1
         # case where both lists are same length
        if len(nums1) == len(nums2):
           return (nums1[l2] + nums2[r1]) / 2

        total_len = len(nums1) + len(nums2)

        # case where one list is empty?
         
        # case where both lists are len 1

        # case where len odd

        # case where len even






sol = Solution()

print(sol.findMedianSortedArrays(nums1 = [1,3], nums2 = [2])) # 2.00000

print(sol.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4])) # 2.50000

print(sol.findMedianSortedArrays(nums1 = [1], nums2 = [2])) # 1.50000