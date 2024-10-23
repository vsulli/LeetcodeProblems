# 74 Search a 2D Matrix

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # figure out which row it needs to be in, then do binary search on that row
        # log m + log n
        ROWS, COLS = len(matrix), len(matrix[0])

        # look for row you need
        # two pointers
        top, bot = 0, ROWS - 1
        while top <= bot:
            mid_row = (top + bot) // 2
            if target > matrix[mid_row][-1]: # rightmost value in row
                top = mid_row + 1 # going down creates larger values
                # look at rows that are larger
            elif target < matrix[mid_row][0]:
                bot = mid_row - 1
            else: # target is in range
                break 

        
        if not (top <= bot):
            return False # target does not appear in matrix
        
        # run binary search on middle row
        row = (top + bot) // 2
        l, r = 0, COLS - 1 # rightmost number in row
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1 # search to right
            elif target < matrix[row][m]:
                r = m - 1 # search to left
            else:
                return True
        
        return False




sol = Solution()

print(sol.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3)) # true

print(sol.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13)) # false
