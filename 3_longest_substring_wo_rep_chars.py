# TODO WIP
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
        seen = [] 
        max_len = 0
        for i in range(len(s)):

            if s[i] not in seen:
                seen.append(s[i])
                max_len = max(max_len, len(seen))
            elif i+1 < len(s) -1 and s[i+1] in seen:
                # reset set from index of same onwards
                seen = seen[seen.index(s[i+1]):]
                seen.append(s[i])
                max_len = max(max_len, len(seen))
            else:
                seen.append(s[i])
                max_len = max(max_len, len(seen))
        return max_len
      # loop through all characters
      # keep track of substring with set? 
      # keep track of max_len
      # if next letter encountered is already in set, reset
      # after adding to set, check length, if greater than current, update?
    

         

sol = Solution()

print(sol.lengthOfLongestSubstring(s = "abcabcbb")) # 3

print(sol.lengthOfLongestSubstring(s ="cdd")) # 2

print(sol.lengthOfLongestSubstring(s = "bbbbb")) # 1

print(sol.lengthOfLongestSubstring(s = "pwwkew")) # 3

print(sol.lengthOfLongestSubstring("dvdf")) # 3

print(sol.lengthOfLongestSubstring("")) # 0