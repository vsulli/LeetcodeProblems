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
        # left pointer, need to keep track of count of letters?
        t_dict = Counter(t).most_common() # [('A', 1), ('B', 1), ('C', 1)]
        count = 0
        l = 0
        res = ""
        res_dict = {}
        for r in range(len(s)):
            # add character to result string
            res += s[r]

            # if that character that was just added is part of the t string, add to dict
            if s[r] in t:
                if s[r] in res_dict:
                    res_dict[s[r]] += 1
                else:
                    res_dict[s[r]] = 1
            # check if res_dict matches t_dict
            if res_dict == t_dict:
                # set count equal to length of dict
        
        # take off letters from result while still matches t count
        while True:
            
            res -= res[l]
        return res
        

sol = Solution()

print(sol.minWindow(s = "ADOBECODEBANC", t = "ABC")) # "BANC"
# smallest window that includes all the letters of t

print(sol.minWindow(s = "a", t = "a")) # "a"  entire substring is minimum window

print(sol.minWindow(s = "a", t = "aa")) # "" 
# both a's from t have to be included 