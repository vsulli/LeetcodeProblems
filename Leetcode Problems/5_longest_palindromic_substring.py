'''
Longest Palindromic Substring
Leetcode # 5
vsulli
19 September 2024

Given a string s, return the longest palindromic substring in s.

'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd length 
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r <len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res

sol = Solution()


print(sol.longestPalindrome(s = "babad")) # bab or aba

print(sol.longestPalindrome(s = "cbbd")) # bb