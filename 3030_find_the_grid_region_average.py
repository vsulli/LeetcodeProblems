# TODO notate solution
'''
Find the Grid of Region Average
Leetcode # 3030
vsulli
15 September 2024

You are given m x n grid image which represents a grayscale 
image, where image[i][j] represents a pixel with intensity 
in the range [0..255]. You are also given a non-negative 
integer threshold.

Two pixels are adjacent if they share an edge.

A region is a 3 x 3 subgrid where the absolute difference 
in intensity between any two adjacent pixels is less than 
or equal to threshold.

All pixels in a region belong to that region, note that a 
pixel can belong to multiple regions.

You need to calculate a m x n grid result, where result[i][j] 
is the average intensity of the regions to which image[i][j] 
belongs, rounded down to the nearest integer. If image[i][j] 
belongs to multiple regions, result[i][j] is the average of the 
rounded-down average intensities of these regions, rounded down 
to the nearest integer. If image[i][j] does not belong to any 
region, result[i][j] is equal to image[i][j].

Return the grid result.
'''

from typing import List


class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        # image[a][b] and image[c][d] two pixels are adjacent if |a - c| + | b - d| == 1
        m, n = len(image), len(image[0])
        res = [[0 for _ in range(n)] for _ in range(m)]
        cnt = [[0 for _ in range(n)] for _ in range(m)]
        def isValid(x, y):
            for dx in [-1, 1]:
                for dy in [-1, 1]:
                    if not (abs(image[x][y] - image[x+dx][y]) <= threshold and abs(image[x][y] - image[x][y+dy]) <= threshold):
                        return False
            if not (abs(image[x-1][y-1] - image[x-1][y]) <= threshold and abs(image[x-1][y-1] - image[x][y-1]) <= threshold):
                return False
            if not (abs(image[x-1][y+1] - image[x-1][y]) <= threshold and abs(image[x-1][y+1] - image[x][y+1]) <= threshold):
                return False
            if not (abs(image[x+1][y-1] - image[x+1][y]) <= threshold and abs(image[x+1][y-1] - image[x][y-1]) <= threshold):
                return False
            if not (abs(image[x+1][y+1] - image[x+1][y]) <= threshold and abs(image[x+1][y+1] - image[x][y+1]) <= threshold):
                return False
            return True
            
        for i in range(1, m-1):
            for j in range(1, n-1):
                if isValid(i, j):
                    val = 0
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            cnt[i+dx][j+dy] += 1
                            val += image[i+dx][j+dy]
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            res[i+dx][j+dy] += val // 9
                
                
        for i in range(m):
            for j in range(n):
                if cnt[i][j] == 0:
                    res[i][j] = image[i][j]
                else:
                    res[i][j] //= cnt[i][j]
        
        return res


sol = Solution()

print(sol.resultGrid(image = [[5,6,7,10],[8,9,10,10],[11,12,13,10]], threshold = 3))
# Output: [[9,9,9,9],[9,9,9,9],[9,9,9,9]]

print(sol.resultGrid(image = [[10,20,30],[15,25,35],[20,30,40],[25,35,45]], threshold = 12))
# Output: [[25,25,25],[27,27,27],[27,27,27],[30,30,30]]

print(sol.resultGrid([[5,6,7],[8,9,10],[11,12,13]], threshold = 1))
# Output: [[5,6,7],[8,9,10],[11,12,13]]