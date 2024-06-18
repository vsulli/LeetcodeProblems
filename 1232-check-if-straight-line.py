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
        # per constraints, will always have at least 2 points
        # loop through every index
        # formula for slope = rise / run 
        slope = ((coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])) 
        for i in range(1, len(coordinates)):
            pass
        # if slope is different than previously calculated, return false
        return True
        # approach 2 - calculate the slope for every point, need to match

sol = Solution()

'''
print(sol.checkStraightLine(coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]])) # true

print(sol.checkStraightLine(coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]])) # false
'''
print(sol.checkStraightLine(coordinates = [[0,0],[0,1],[0,-1]])) # true
