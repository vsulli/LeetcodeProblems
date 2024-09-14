# TODO learn how to sort a hashmap in descending order
'''
Top K Frequent Words
Leetcode # 692
vsulli
14 September 2024

Given an array of strings words and 
an integer k, return the k most 
frequent strings.

Return the answer sorted by the 
frequency from highest to lowest. 
Sort the words with the same frequency 
by their lexicographical order.
'''

from heapq import *
from typing import Counter, List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Make a dictionary of counts
        freq_dict = Counter(words)
        
        # Find max frequency
        max_freq = max(freq_dict.values())
        
        # Make Max frequency + 1 buckets
        buckets = [[] for _ in range(max_freq + 1)]

        # Heap push word/key in bucket corresponding to freq
        for key, val in freq_dict.items():
            heappush(buckets[val], key)
        
        ans = []
        bucket_index = max_freq
        while k > 0 :
            if len(buckets[bucket_index]) > 0:
                ans.append(heappop(buckets[bucket_index]))
                k -= 1
            else:
                bucket_index -= 1
            
        return ans

       

sol = Solution()

print(sol.topKFrequent(words = ["i","love","leetcode","i","love","coding"], k = 3)) # Output: ["i","love","coding"]

print(sol.topKFrequent(words = ['i'], k = 1)) # Output: ['i']

print(sol.topKFrequent(words = ["i","love","leetcode","i","love","coding"], k = 2)) # Output: ["i","love"]

print(sol.topKFrequent(words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4)) # Output: ["the","is","sunny","day"]