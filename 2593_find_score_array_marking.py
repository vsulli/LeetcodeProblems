'''
Find Score of an Array After Marking
All Elements
Leetcode # 2593
vsulli
13 December 2024

You are given an array nums consisting 
of positive integers.

Starting with score = 0, apply the following 
algorithm:

Choose the smallest integer of the array that 
is not marked. If there is a tie, choose the 
one with the smallest index.
Add the value of the chosen integer to score.
Mark the chosen element and its two adjacent 
elements if they exist.
Repeat until all the array elements are marked.
Return the score you get after applying the 
above algorithm.
'''
from typing import List

class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        visited = set() # while length of visited less than length nums keep going?
        # can't sort, have to find smallest, then mark it and 2 adjacent if they exist
        
        # find smallest
            # if tie, choose smaller index
        # how to mark as visited?
        while len(visited) < len(nums):
            # locate smallest index
            smallest_index = nums.index(min(nums))
            score += nums[smallest_index]

            # add smallest index and adjacent to visited
            visited.add(smallest_index)

            nums[smallest_index] = float("inf")
            if smallest_index - 1 >= 0 and smallest_index - 1 not in visited:
                visited.add(smallest_index - 1)
                nums[smallest_index - 1] = float("inf")

            if smallest_index + 1 < len(nums) and smallest_index + 1 not in visited:
                visited.add(smallest_index + 1)
                nums[smallest_index + 1] = float("inf")
        
        return score
            

sol = Solution()

print(sol.findScore(nums = [2,1,3,4,5,2]))

print(sol.findScore(nums = [2,3,5,1,3,2]))