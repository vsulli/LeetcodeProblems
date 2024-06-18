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
        try:
            slope = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0]) 
        except ZeroDivisionError:
            slope = 0
        last_point = coordinates[1]
        for i in range(2,len(coordinates)):
            try:
                if (coordinates[i][1] - last_point[1]) / (coordinates[i][0] - last_point[0]) != slope:
                    return False
            except ZeroDivisionError:
                if 0 != slope:
                    return False
        return True
       

sol = Solution()

print(sol.checkStraightLine(coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]])) # true

print(sol.checkStraightLine(coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]])) # false

print(sol.checkStraightLine(coordinates = [[0,0],[0,1],[0,-1]])) # true

print(sol.checkStraightLine(coordinates = [[-3,-2],[-1,-2],[2,-2],[-2,-2],[0,-2]])) # true
# slope of 0