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
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countT , window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0) # default value of 0 if it doesn't exist

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                # pop from left of window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res   
        return s[l:r+1]

sol = Solution()

print(sol.minWindow(s = "ADOBECODEBANC", t = "ABC")) # "BANC"
# smallest window that includes all the letters of t

print(sol.minWindow(s = "a", t = "a")) # "a"  entire substring is minimum window

print(sol.minWindow(s = "a", t = "aa")) # "" 
# both a's from t have to be included 