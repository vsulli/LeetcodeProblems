'''
Range Sum Query 2D - Immutable
Leetcode # 304
vsulli
27 June 2024

Given a 2D matrix matrix, handle multiple 
queries of the following type:

Calculate the sum of the elements of matrix 
inside the rectangle defined by its upper 
left corner (row1, col1) and lower right 
corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the 
object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, 
int col2) Returns the sum of the elements of 
matrix inside the rectangle defined by its 
upper left corner (row1, col1) and lower 
right corner (row2, col2).
You must design an algorithm where sumRegion 
works on O(1) time complexity.

'''

class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix
        # create prefix sum matrix?
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        pass
        # will have to initialize a dummy row above top row and to left?



# Your NumMatrix object will be instantiated and called as such:
obj = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
print(obj.sumRegion(2,1,4,3))