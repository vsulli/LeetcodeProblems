
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
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        pass

sol = Solution()

print(sol.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3)) # true

print(sol.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13)) # false