'''
Longest Palindromic Substring
Leetcode # 5
vsulli
19 September 2024

Given a string s, return the longest palindromic substring in s.

'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # two pointers
        # start one pointer at end of string
        res = ''
        p = len(s) - 1

        for i in range(len(s)):
            res += s[i]
            # check if it's a palindrome by getting from middle index to end(reverse order) and beg to middle index
            
        

sol = Solution()

print(sol.longestPalindrome(s = "babad")) # bab or aba

print(sol.longestPalindrome(s = "cbbd")) # bb