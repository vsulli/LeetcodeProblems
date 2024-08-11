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
# sliding window
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0) # set value in hashmap, 0 default value

            # make sure current window is valid
            while (r - l + 1) - max(count.values()) > k: # more replacements than allowed
                count[s[l]] -= 1
                l += 1 
            res = max(res, r - l + 1) # r - l + 1 is size of window
        return res
            

sol = Solution()

print(sol.characterReplacement(s = "ABAB", k = 2))
# 4 - replace either 2 A's or 2 B's

print(sol.characterReplacement(s = "AABABBA", k = 1))
# 4 - replace one A in the middle to B