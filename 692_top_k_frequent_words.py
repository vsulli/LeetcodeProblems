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

from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        pass

sol = Solution()

print(sol.topKFrequent(words = ["i","love","leetcode","i","love","coding"], k = 2))

print(sol.topKFrequent(words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4))