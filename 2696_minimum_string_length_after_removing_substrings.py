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

class Solution:
    def minLength(self, s: str) -> int:
        pass

sol = Solution()

print(sol.minLength(s = "ABFCACDB")) # 2

print(sol.minLength(s = "ACBBD")) # 5