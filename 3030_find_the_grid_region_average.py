'''
Search a 2D Matrix
Leetcode # 74
vsulli
13 September 2024

You are given an m x n integer matrix with the following properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than 
the last integer of the previous row.
Given an integer target, return true if target 
is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
'''

from typing import List


class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        pass


sol = Solution()

print(sol.resultGrid(image = [[5,6,7,10],[8,9,10,10],[11,12,13,10]], threshold = 3))

print(sol.resultGrid(image = [[10,20,30],[15,25,35],[20,30,40],[25,35,45]], threshold = 12))