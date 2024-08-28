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


class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        count = 0
        curSum = sum(arr[:k - 1])
        # just one pointer up to length - k index
        for L in range(len(arr)- k + 1):
            curSum += arr[L + k - 1]
            if (curSum / k ) >= threshold:
                count += 1
            curSum -= arr[L]

        return count


sol = Solution()

print(sol.numOfSubarrays(arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4)) # output: 3

print(sol.numOfSubarrays(arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5)) # output: 6

print(sol.numOfSubarrays(arr = [3], k = 1, threshold = 3)) # 1