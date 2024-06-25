'''
Container with Most Water
Leetcode # 11
vsulli
25 June 2024

integer array height of length n
n vertical lines drawn such that 
the two endpoints of the ith line are (i, 0) 
and (i, height[i])

find two lines that together with the x-axis form a container
such that the container contains the most water

return the maximum amount of water a container can store

'''

class Solution:
    def maxArea(self, height: list[int]) -> int:
        pass
        # index i is the x distance
        # need to loop through height
        # need to find max height and index
        # need to find 2nd highest

        # find max
        # check for another high one that is at its same level
            # if not, then find 2nd highest that is farthest away
            # calculate area using min of the two and x distance between them

sol = Solution()

print(sol.maxArea(height = [1,8,6,2,5,4,8,3,7])) # 49

print(sol.maxArea(height = [1,1])) # 1 