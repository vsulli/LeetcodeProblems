
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
            # if in range of that row search by regular binary search
            if  matrix[mid_row][l] <= target <= matrix[mid_row][r]:
                # binary search
                # if found in range, set contains_target to True and break
                while l <= r:
                    
                    m = (l + r) // 2
                    if matrix[mid_row][m] > target:
                        r = m - 1
                    elif matrix[mid_row][m] < target:
                        l = m + 1
                    # found it
                    else:
                        return True
                return False
            # if smaller, assign to smaller matrix
            elif target < matrix[mid_row][l]:
                mr = mid_row - 1
            # if larger, assign to larger matrix
            elif target > matrix[mid_row][r]:
                ml = mid_row + 1

        return contains_target


sol = Solution()

print(sol.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3)) # true

print(sol.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13)) # false