'''
Trapping Rain Water
Leetcode # 42
vsulli
26 June 2024

Given n non-negative integers, representing an 
elevation map where the width of each bar is 1, compute how much water
it can trap after raining
'''

class Solution:
    def trap(self, height: list[int]) -> int:
        # two pointers l and r
        # in order to count as water container, must have columns left and right of it of at least equal height
        # check slice between larger columns to subtract out  squares? or 
        # just subtract that out

        # initialize pointer to 0 and 2?
        # if len(height) < 3 return 0

        water_contained = 0
        
        l, r = 0, len(height) - 1
        if height[l] == 0:
            l +=1
        if height[r] == 0:
            r -=1
        # while l < r:
        # water contained is the height of lowest column * difference in index
        # subtract sliced sum of inbetween indices
        water = (min(height[l], height[r]) * (r - l)) - 1 - sum(i for i in range(l+1, r) if height[i] == 1)
        print(water)



sol = Solution()

print(sol.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1])) # 6

print(sol.trap(height = [4,2,0,3,2,5])) # 9