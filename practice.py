# sliding window technique video lesson
# https://www.youtube.com/watch?v=dOonV4byDEg&ab_channel=ProfoundAcademy
from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        currSum = sum(arr[:k])
        if (currSum / k) >= threshold:
                count += 1

        for r in range(k, len(arr)):
            currSum += arr[r] - arr[r - k]
            if (currSum / k) >= threshold:
                count += 1
        return count


sol = Solution()

print(sol.numOfSubarrays(arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4)) # output: 3

print(sol.numOfSubarrays(arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5)) # output: 6

print(sol.numOfSubarrays(arr = [3], k = 1, threshold = 3)) # 1
