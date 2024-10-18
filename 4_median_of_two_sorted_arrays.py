
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
        pass


sol = Solution()

print(sol.findMedianSortedArrays(nums1 = [1,3], nums2 = [2])) # 2.00000

print(sol.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4])) # 2.50000