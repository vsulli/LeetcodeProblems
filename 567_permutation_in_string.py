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

from itertools import permutations

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # how to create all permutations?
        # recursive?
        # check as permutations created if they're in s2
        isSubstring = False

        for p in permutations(s1):
            if ''.join(p) in s2:
                return True


        return isSubstring

sol = Solution()

print(sol.checkInclusion(s1 = "ab", s2 = "eidbaooo")) # true
# one permutation exists - ba

print(sol.checkInclusion(s1 = "ab", s2 = "eidboaoo")) # false
