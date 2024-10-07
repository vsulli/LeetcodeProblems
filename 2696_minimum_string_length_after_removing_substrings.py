'''
Minimum String Length After Removing Substrings
Leetcode # 2696
vsulli
7 October 2024

You are given a string s consisting only of uppercase 
English letters.

You can apply some operations to this string 
where, in one operation, you can remove any 
occurrence of one of the substrings "AB" or "CD" from s.

Return the minimum possible length of the 
resulting string that you can obtain.

Note that the string concatenates after removing 
the substring and could produce new "AB" or "CD" substrings.
'''

import re

class Solution:
    def minLength(self, s: str) -> int:
        # while loop while AB or CD is in s
        # once neither substring appears, return length of s

        while True:
            if not 'AB' in s and not 'CD' in s:
                return len(s)
            if 'AB' in s:
                s = re.sub('AB', '', s)
            if 'CD' in s:
                s = re.sub('CD', '', s)

sol = Solution()

print(sol.minLength(s = "ABFCACDB")) # 2 'FC'

print(sol.minLength(s = "ACBBD")) # 5