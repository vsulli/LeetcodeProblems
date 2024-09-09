
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

        # first row minus last column
        res = []
        for n in range(len(matrix[0]) - 1):
            res.append(matrix[0][n])

        while True:
            
        
        
        '''
        for row in range(len(matrix[0])):
            for column in range(len(matrix[1])):
                print(matrix[row][column])
                '''
        
        return res

sol = Solution()

print(sol.spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))


print(sol.spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
