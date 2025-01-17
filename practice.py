from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        s_freq = sorted(freq.items(), key=lambda items: items[1], reverse=True)
        for i, key in enumerate(s_freq):
            res.append(key[0])
            if i == k-1:
                return res

sol = Solution()

print(sol.topKFrequent(nums = [1,1,1,2,2,3], k = 2))

print(sol.topKFrequent(nums = [1], k = 1))