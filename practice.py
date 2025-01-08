# 347 Top K Frequent Elements

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        for n in nums:
            if n in num_count:
                num_count[n] += 1
            else:
                num_count[n] = 1
        sorted_num_count = sorted(num_count.items(), key=lambda items:items[1], reverse=True)
        res = []
        for i, n in enumerate(sorted_num_count):
            res.append(n[0])
            if i == k - 1:
                return res


sol = Solution()

print(sol.topKFrequent(nums = [1,1,1,2,2,3], k = 2))

print(sol.topKFrequent(nums = [1], k = 1))