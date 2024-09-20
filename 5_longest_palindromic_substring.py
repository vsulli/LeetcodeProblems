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
        m = len(s) // 2
        p = len(s) - 1
        if s[m::-1] == s[m:p+1]:
            res = s[m:p+1]
        p-=1

        for i in range(len(s)):
            # print(s[m:i:-1])
            # print(s[m:p+1])
            # slice string in neg direction
            if s[m:i:-1] == s[m:p+1]:
                print(s[m:i:-1])
                print(s[m:p+1])
                print("---------")
                if len(s) // 2 == 0:
                    new_res = s[m:p+1] # if even length string
                elif len(s) // 2 != 0:
                    new_res = s[m-1:p+1] # if odd length string
                if len(new_res) > len(res):
                    res = new_res
                
            # check if it's a palindrome by getting from middle index to end(reverse order) and beg to middle index
            p-=1
        return res

sol = Solution()

'''

print(sol.longestPalindrome(s = "babad")) # bab or aba
'''

print(sol.longestPalindrome(s = "cbbd")) # bb