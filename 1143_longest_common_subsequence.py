'''
Longest Common Subsequence
Leetcode # 1143
vsulli
22 September 2024

Given two strings text1 and text2, return the 
length of their longest common subsequence. 
If there is no common subsequence, return 0.

A subsequence of a string is a new string 
generated from the original string with some 
characters (can be none) deleted without changing 
the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a 
subsequence that is common to both strings.
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        res = ""
        resLen = 0
        p1, p2 = 0, 0
        for i in range(len(text1)):
            while p2 < len(text2) and text2[p2] != text1[i]:
                p2 += 1
            # match found, meaning that p1 now needs to move to p2
            if p2 < len(text2) and text1[i] == text2[p2]:
                resLen += 1
                res += text2[p2]
                # move to position after match
                p1 = p2 + 1
            p2 = p1
        print(res)
        return resLen

sol = Solution()

print(sol.longestCommonSubsequence(text1 = "abcde", text2 = "ace" )) # Output: 3  "ace"

print(sol.longestCommonSubsequence(text1 = "abc", text2 = "abc")) # Output: 3 "abc"

print(sol.longestCommonSubsequence(text1 = "abc", text2 = "def")) # Output: 0

print(sol.longestCommonSubsequence(text1 = "ezupkr", text2 = "ubmrapg")) # Output: 2

print(sol.longestCommonSubsequence(text1 = "bsbininm", text2 = "jmjkbkjkv")) # Output: 1