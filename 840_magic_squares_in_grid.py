''' 
Magic Squares in Grid
Leetcode # 840
vsulli
9 August 2024

A 3 x 3 magic square is a 3 x 3 
grid filled with distinct numbers 
from 1 to 9 such that each row, 
column, and both diagonals all 
have the same sum.

Given a row x col grid of integers, 
how many 3 x 3 contiguous magic 
square subgrids are there?

Note: while a magic square can 
only contain numbers from 1 to 9, 
grid may contain numbers up to 15.
 
'''

class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        # row
        for x in range(0, len(grid[0])):
            # column
            for y in range(0, len(grid[1])):
                print(grid[x][y])

sol = Solution()

print(sol.numMagicSquaresInside(grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]))