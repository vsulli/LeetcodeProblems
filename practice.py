# sliding window technique video lesson
# https://www.youtube.com/watch?v=dOonV4byDEg&ab_channel=ProfoundAcademy
from typing import List


class Solution:
    def maxofSubarray(self, arr: List[int], k: int) -> int:
        # given an array of nums
        # calculate the maximum of a subarray given size of window k 
        currSum = sum(arr[:k - 1])
        currMax = currSum

        for L in range(len(arr) - k + 1):
            currSum += arr[L + k - 1]
            if currSum > currMax:
                currMax = currSum
            currSum -= arr[L]

        return currMax


sol = Solution()

print(sol.maxofSubarray(arr = [8, 3, -2, 4, 5, -1, 0, 5, 3, 9, -6], k = 5)) # 18, 

print(sol.maxofSubarray(arr = [11,13,17,23,29,31,7,5,2,3], k = 5)) 

