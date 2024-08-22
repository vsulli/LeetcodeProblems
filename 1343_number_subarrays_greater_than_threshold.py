'''
Number of Sub-arrays of Size K and Average
Greater than or Equal to Threshold
Leetcode # 1343
vsulli
21 August 2024

Given an array of integers arr and two 
integers k and threshold, return the number 
of sub-arrays of size k and average greater 
than or equal to threshold.
'''

import statistics

class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        left = 0
        right = k
        count = 0

        while right != len(arr):
            average = statistics.mean(arr[left:right])
            if average >= threshold:
                count +=1
            
            left += 1
            right += 1

        return count


sol = Solution()

print(sol.numOfSubarrays(arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4)) # output: 3

print(sol.numOfSubarrays(arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5)) # output: 6

print(sol.numOfSubarrays(arr = [3], k = 1, threshold = 3)) # 1