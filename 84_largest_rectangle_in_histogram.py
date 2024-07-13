'''
Largest Rectangle in Histogram
Leetcode # 84
vsulli
13 July 2024

Given an array of integers heights 
representing the histogram's bar 
height where the width of each bar 
is 1, return the area of the largest 
rectangle in the histogram.
'''

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # given heights, each width is 1
        # need to loop through 
        # indices that are adjacent will take the lowest of adjacent
        # to calculate area
        max_area = max(heights)

        for i in range(len(heights)-1):
            j = i+1
            area = min(heights[i], heights[j]) * 2
            max_area = max(area, max_area)
        return max_area




sol = Solution()

print(sol.largestRectangleArea(heights = [2,1,5,6,2,3])) # 10

print(sol.largestRectangleArea(heights = [2,4])) # 4

print(sol.largestRectangleArea(heights = [0,9])) # 9