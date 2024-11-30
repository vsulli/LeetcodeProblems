#347 top k frequent elements
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counts = {} # num: count
        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
        sorted_counts = sorted(counts.items(), key=lambda items:items[1], reverse=True)
        for i,n in enumerate(sorted_counts):
            res.append(n[0])
            if i == k - 1:
                return res



sol = Solution()

print(sol.topKFrequent(nums = [1,1,1,2,2,3], k = 2))