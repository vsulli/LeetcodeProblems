
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
        # need to select middle of middle array?
        # need to maintain 2 pointers to beginning and end of that row of matrix?
        # if m isn't in that range then set to lower or higher row?
        # it is possible for no answer to be found

        contains_target = False
        # assign to middle matrix
        l, r = 0,len(matrix[0]) - 1

        ml, mr = 0, len(matrix) - 1
        mid_row = (ml + mr) // 2
        while l <= r:
            mid_row = (ml + mr) // 2
            # if target is in that row
            if  matrix[mid_row][l] <= target <= matrix[mid_row][r]:
                print("in row")
                return
            elif target < matrix[mid_row][l]:
                mr = mid_row - 1
            elif target > matrix[mid_row][r]:
                ml = mid_row + 1
                
        


        # if in range of that row search by regular binary search

        # if smaller, assign to smaller matrix

        # if larger, assign to larger matrix
        return contains_target


sol = Solution()

print(sol.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3)) # true

print(sol.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13)) # false