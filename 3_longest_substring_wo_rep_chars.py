'''
Longest Substring without Repeating Characters
Leetcode # 3
vsulli
30 June 2024

Given a string s, find the length of the longest 
substring
 without repeating characters.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_len = 0
        for c in s:
            if c in seen:
                # reset set
                seen = set()
                seen.add(c)
                max_len = max(max_len, len(seen))
            else:
                seen.add(c)
                max_len = max(max_len, len(seen))
        return max_len
      # loop through all characters
      # keep track of substring with set? 
      # keep track of max_len
      # if next letter encountered is already in set, reset
      # after adding to set, check length, if greater than current, update?
    

         

sol = Solution()

print(sol.lengthOfLongestSubstring(s = "abcabcbb")) # 3

print(sol.lengthOfLongestSubstring(s = "bbbbb")) # 1

print(sol.lengthOfLongestSubstring(s = "pwwkew")) # 3

print(sol.lengthOfLongestSubstring("dvdf")) # 3