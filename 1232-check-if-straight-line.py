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

        # undefined line - division by 0, check if all 0's and return true?
        # formula for slope = rise / run 
        old_denom = (coordinates[1][0] - coordinates[0][0]) # diff x values
    
        if old_denom > 0:
            old_slope = ((coordinates[1][1] - coordinates[0][1]) / old_denom) 
       
        for i in range(1, len(coordinates)):
            denom = (coordinates[i][0] - coordinates[i-1][0]) # diff x values
            if denom > 0:
                slope = ((coordinates[i][1] - coordinates[i-1][1]) / denom) 
                      
            if denom != old_denom or (denom > 0 and slope != old_slope):
                return False
            
            
        # if slope is different than previously calculated, return false
        return True
       

sol = Solution()


print(sol.checkStraightLine(coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]])) # true

print(sol.checkStraightLine(coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]])) # false

print(sol.checkStraightLine(coordinates = [[0,0],[0,1],[0,-1]])) # true
