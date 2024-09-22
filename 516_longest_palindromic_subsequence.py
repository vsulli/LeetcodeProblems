'''
Longest Palindromic Subsequence
Leetcode # 516
vsulli
22 September 2024

Given a string s, find the longest palindromic 
subsequence's length in s.

A subsequence is a sequence that can be 
derived from another sequence by deleting 
some or no elements without changing the order 
of the remaining elements.

'''

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # similar to # 5
        # make a copy of s
        # when checking if next letter matches, if it doesn't, 
        # delete that character and check next one until it does match or you reach end of string?

        res = ""
        resLen = 0

        for i in range(len(s)):

            # odd number s
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resLen:
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even number s
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resLen:
                    resLen = r - l + 1
                l -= 1
                r += 1
            


        return resLen

sol = Solution()

print(sol.longestPalindromeSubseq(s = "bbbab"))

print(sol.longestPalindromeSubseq(s = "cbbd"))
