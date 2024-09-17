'''
Uncommon Words from Two Sentences
Leetcode # 884
vsulli
17 September 2024

A sentence is a string of single-space 
separated words where each word consists 
only of lowercase letters.

A word is uncommon if it appears exactly 
once in one of the sentences, and does 
not appear in the other sentence.

Given two sentences s1 and s2, return a 
list of all the uncommon words. You may 
return the answer in any order.
'''

from collections import defaultdict
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count = defaultdict(int)
        for w in s1.split(" ") + s2.split(" "):
            count[w] += 1

        res = []
        for w, cnt in count.items():
            if cnt == 1:
                res.append(w)

        return res

        

sol = Solution()

print(sol.uncommonFromSentences(s1 = "this apple is sweet", s2 = "this apple is sour")) 
# Output: ["sweet", "sour"]

print(sol.uncommonFromSentences(s1 = "apple apple", s2 = "banana"))
# Output: ["banana"]