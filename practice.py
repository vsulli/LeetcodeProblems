# sliding window technique video lesson
# https://www.youtube.com/watch?v=dOonV4byDEg&ab_channel=ProfoundAcademy



from typing import List

# find longest subarray that has a sum less than "s"
class Solution:
    def longestSubarraySum(self, arr: List[int], s: int) -> int:
        # initialize left pointer, current sum, and max length
        l, currSum, maxLen = -1, 0, 0
        for r in range(len(arr)):
            currSum += arr[r]
            while currSum >= s: # adjust subarray while sum greater than s
                l += 1
                currSum -= arr[l]
            # update max length
            maxLen = max(maxLen, r - l) # take right index minus left index
        return maxLen


sol = Solution()

print(sol.longestSubarraySum(arr = [4, 5, 2, 0, 1, 8, 12, 3, 6, 9], s = 15)) # 5