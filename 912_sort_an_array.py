''' 
Sort an Array
Leetcode # 912
vsulli
25 July 2024

Given an array of integers 
nums, sort the array in 
ascending order and return it.

You must solve the problem 
without using any built-in 
functions in O(nlog(n)) time 
complexity and with the smallest 
space complexity possible.
'''

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
      # can't use built-in functions
      # has to be O(nlog(n)) 
      # use some kind of binary search?
      pass

sol = Solution()

print(sol.sortArray(nums = [5,2,3,1])) # [1,2,3,5] 
# positions of some numbers aren't changed (2,3)
# 1 and 5 swapped

