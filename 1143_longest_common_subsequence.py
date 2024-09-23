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

# bottom up dynamic programming
# 2D grid
# O(n * m)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        # iterate through 2d grid in reverse order
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) -1, -1, -1):
                # if they match
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i +1][j + 1] # 1 + diagonal
                else:
                    # max to right or below
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        # top left is result
        return dp[0][0]
                    
sol = Solution()

print(sol.longestCommonSubsequence(text1 = "abcde", text2 = "ace" )) # Output: 3  "ace"

print(sol.longestCommonSubsequence(text1 = "abc", text2 = "abc")) # Output: 3 "abc"

print(sol.longestCommonSubsequence(text1 = "abc", text2 = "def")) # Output: 0

print(sol.longestCommonSubsequence(text1 = "ezupkr", text2 = "ubmrapg")) # Output: 2

print(sol.longestCommonSubsequence(text1 = "bsbininm", text2 = "jmjkbkjkv")) # Output: 1

print(sol.longestCommonSubsequence(text1 = "oxcpqrsvwf", text2 = "shmtulqrypy")) # Output: 2