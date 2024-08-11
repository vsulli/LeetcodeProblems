''' 
Longest Repeating Character Replacement
Leetcode # 424
vsulli
10 August 2024

You are given a string s and 
an integer k. You can choose 
any character of the string 
and change it to any other 
uppercase English character. 
You can perform this operation 
at most k times.

Return the length of the longest 
substring containing the same letter 
you can get after performing the 
above operations.
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        pass

sol = Solution()

print(sol.characterReplacement(s = "ABAB", k = 2))
# 4

print(sol.characterReplacement(s = "AABABBA", k = 1))
# 4