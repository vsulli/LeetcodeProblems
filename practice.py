# 347 Top K Frequent Elements

from typing import List
class Solution:
    def topKFrequent(self, nums:List[int], k:int)->List[int]:
        res = []

        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        
        for i, v in enumerate(d):
            res.append(v)
            if i == k-1:
                return res


sol = Solution()

print(sol.topKFrequent(nums = [1,1,1,2,2,3], k = 2)) # [1, 2]

print(sol.topKFrequent(nums = [1], k = 1)) # [1]