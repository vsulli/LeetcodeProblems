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

from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # loop through words
        # if a word hasn't been seen, add to hashmap
        # if it already has, increment its value
        # then sort the hashmap and return highest ones for k
        res = []
        freq = {}
        for w in words:
            if w in freq:
                freq[w] += 1
            else:
                freq[w] = 1
        
        sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        # sorted_keys = sorted_freq.keys()
        res = list(sorted_freq.keys())[:k]

        return res

sol = Solution()

print(sol.topKFrequent(words = ['i'], k = 1))

print(sol.topKFrequent(words = ["i","love","leetcode","i","love","coding"], k = 2))

print(sol.topKFrequent(words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4))