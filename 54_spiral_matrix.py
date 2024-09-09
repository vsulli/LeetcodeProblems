
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
        # use four pointers
        # always start at top left position
        # O(m * n) time complexity, O(1) memory

        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # get every value in top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1


            # get every i in right col
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            # get every i in bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1


            # get every i in left col
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res







sol = Solution()


print(sol.spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))


print(sol.spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
