'''
Permutation in String
Leetcode # 567
vsulli
21 August 2024

Given two strings s1 and s2, 
return true if s2 contains 
a permutation of s1, or false 
otherwise.

In other words, return true if
 one of s1's permutations is 
 the substring of s2.
'''

from collections import Counter

        
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # slide through s2 O(n) going by length of s1
        # check if count of each character matches count of s1
        isSubstring = False
        l = 0
        count = {}
        for c in s1:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1

        counter = Counter(s2)
        for r in range(len(s1)-1, len(s2), len(s1)):
            for char in count:
                if counter[char] == count[char]

        return isSubstring

sol = Solution()

print(sol.checkInclusion(s1 = "ab", s2 = "eidbaooo")) # true
# one permutation exists - ba

print(sol.checkInclusion(s1 = "ab", s2 = "eidboaoo")) # false
