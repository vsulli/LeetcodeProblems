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
        # left and right pointers
        l, r = 0, len(height) - 1
        max_area = 0

        while l < r:
            max_area = max(max_area, (min(height[l], height[r])) * (r - l))
            # update side that has lower height, else right
            if height[l] < height[r]:
                l +=1
            else:
                r -=1

        return max_area

sol = Solution()

print(sol.maxArea(height = [1,8,6,2,5,4,8,3,7])) # 49

print(sol.maxArea(height = [1,1])) # 1 