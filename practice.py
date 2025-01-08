# 347 Top K Frequent Elements

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        
        s_count = sorted(count.items(), key=lambda items:items[1], reverse=True)
        res = []
        for i,n in enumerate(s_count):
            res.append(n[0])
            if i == k - 1:
                return res


sol = Solution()

print(sol.topKFrequent(nums = [1,1,1,2,2,3], k = 2))

print(sol.topKFrequent(nums = [1], k = 1))