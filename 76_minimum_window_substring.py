'''
Minimum Window Substring
Leetcode # 76
vsulli
4 September 2024

Given two strings s and t of lengths 
m and n respectively, return the 
minimum window 
substring
 of s such that every character in t 
 (including duplicates) is included in 
 the window. If there is no such substring, 
 return the empty string "".

The testcases will be generated such 
that the answer is unique.
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        pass

sol = Solution()

print(sol.minWindow(s = "ADOBECODEBANC", t = "ABC")) # "BANC"
# smallest window that includes all the letters of t

print(sol.minWindow(s = "a", t = "a")) # "a"  entire substring is minimum window

print(sol.minWindow(s = "a", t = "aa")) # "" 
# both a's from t have to be included 