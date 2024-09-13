
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
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS -1

        while top <= bot:
            row = (top + bot) // 2
            # greater than largest value in row
            if target > matrix[row][-1]:
                top = row + 1
            # less than lowest value in row
            elif target < matrix[row][0]:
                bot = row - 1

            # target value in that row
            else:
                break
        
        # none of rows contain target
        if not (top <= bot):
            return False
        
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                # search right
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1

            else:
                return True
        return False




sol = Solution()

print(sol.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3)) # true

print(sol.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13)) # false