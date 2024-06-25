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
        
        # two pointers?
        # way to store areas and add them upwards?
        # start left and right pointers on outside
        # check from left side scanning right to find what it runs into
        # has to be equal or greater than its height to count
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            max_area = max(max_area, (min(height[l], height[r])) * (r - l))
            if height[l] < height[r]:
                l +=1
            else:
                r -=1

        return max_area

sol = Solution()

print(sol.maxArea(height = [1,8,6,2,5,4,8,3,7])) # 49

print(sol.maxArea(height = [1,1])) # 1 