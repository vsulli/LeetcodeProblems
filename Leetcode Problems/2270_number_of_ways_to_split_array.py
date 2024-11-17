'''
Number of Ways to Split Array
Leetcode # 2270
vsulli
16 September 2024

Given an array of strings words and 
an integer k, return the k most 
frequent strings.

Return the answer sorted by the 
frequency from highest to lowest. 
Sort the words with the same frequency 
by their lexicographical order.
'''

from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # sum of indices up until i are >= all indices to its right?
        count = 0
        prefixSum = 0
        numsSum = sum(nums)
        for i in range(len(nums) - 1):
            prefixSum += nums[i]
            numsSum -= nums[i]
            if prefixSum >= numsSum:
                count +=1
            
        return count

sol = Solution()

print(sol.waysToSplitArray(nums = [10,4,-8,7])) # 2

print(sol.waysToSplitArray(nums = [2,3,1,0])) # 2
