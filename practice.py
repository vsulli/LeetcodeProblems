# leetcode #2554

from typing import List

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
        max_count = 0
        curr_sum = 0
        for i in range(1, n+1):
            if i not in banned_set:
                curr_sum += i
                if curr_sum <= maxSum:
                    max_count += 1
                else:
                    return max_count
        return max_count
            


sol = Solution()


print(sol.maxCount(banned = [1,6,5], n = 5, maxSum = 6))
print(sol.maxCount(banned = [1,2,3,4,5,6,7], n = 8, maxSum = 1))
print(sol.maxCount(banned = [11], n = 7, maxSum = 50))