'''
Check If It Is a Straight Line
Leetcode # 1232
vsulli
17 June 2024

You are given an array coordinates, coordinates[i]  = [x, y]
where [x, y] represents the coordinate of a point

Check if the points make a straight line in the XY plane
'''

class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        # loop through every index
        # check that current both x and y are 1 greater than previous?
        for i in range(1, len(coordinates)):
            if coordinates[i][0] != coordinates[i-1][0] + 1 or coordinates[i][1] != coordinates[i-1][1] + 1:
                return False
        return True
        # approach 2 - calculate the slope for every point, need to match

sol = Solution()

'''
print(sol.checkStraightLine(coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]])) # true

print(sol.checkStraightLine(coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]])) # false
'''
print(sol.checkStraightLine(coordinates = [[0,0],[0,1],[0,-1]])) # true
