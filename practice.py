# leetcode 1343 practice

from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        currSum = sum(arr[:k - 1])

        for L in range(len(arr) - k + 1): # 0 - 5 are values it reaches since 6 is ending
            print("CurrSum " + str(currSum))
            currSum += arr[L + k - 1] # given L of 5, last index will be added here (5+ 3 - 1) = 7
            print("L " + str(L))
            print("CurrSum " + str(currSum))
            print("----------")
            if (currSum / k) >= threshold:
                count += 1
            currSum -= arr[L]
        return count


sol = Solution()

print(sol.numOfSubarrays(arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4)) # 3



print(sol.numOfSubarrays(arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5)) # 6

