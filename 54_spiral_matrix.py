
'''
Spiral Matrix
Leetcode # 54
vsulli
9 September 2024

Given an m x n matrix, return all 
elements of the matrix in spiral order.
'''

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # return the elements fo the matrix in spiral order
        # values from -100 to 100
        # rows/columns from 1 to 10 max
        
        # order will be entire first row, last column, last row
        # then first column up to 2nd row to 2nd to last column

        # assign first row to result
        res = matrix[0]
        
        # total number of elements
        total_len = (len(matrix) * len(matrix[0]))

        count = len(res)

        state = 'column_down'
        offset_row = 1
        offset_column = 0
        row = 1
        column = len(matrix)

        
        for i in range(len(matrix)):
            # switch based on state?
            if state == 'row_right':
                state = 'column_down'

            if state == 'column_down':
                for j in range(column):
                    print(matrix[j][column - offset_column])
                    # res.append()
                state = 'row_left'
            if state == 'row_left':

                state = 'column_up'
            if state == 'column_up':
                state = 'row_right'


        return res





sol = Solution()

'''
print(sol.spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))

'''

print(sol.spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
