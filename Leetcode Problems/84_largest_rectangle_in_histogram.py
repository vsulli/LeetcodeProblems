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
        # O(n) time
        # O(n) memory

        # keep track of max area
        # keep track of which indices' heights go across

        maxArea = 0
        stack = [] # index: height

        for i, h in enumerate(heights):
            start = i
            # pop when stack has height greater than array
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                # extend start index backwards
                start = index
            # add new height to stack, starting at previous index
            stack.append((start, h))


        # if there are rectangles still in stack
        # know they extend full length of array
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea



sol = Solution()

print(sol.largestRectangleArea(heights = [2,1,5,6,2,3])) # 10

print(sol.largestRectangleArea(heights = [2,4])) # 4

print(sol.largestRectangleArea(heights = [0,9])) # 9

print(sol.largestRectangleArea(heights = [2,1,2])) # 3