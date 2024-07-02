
'''
Longest Substring without Repeating Characters
Leetcode # 3
vsulli
2 July 2024

Given a string s, find the length of the longest 
substring
 without repeating characters.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        # set
        n = len(s)
        max_len = 0
        seen = set()
        left = 0

        for right in range(n):
            if s[right] not in seen:
                seen.add(s[right])
                max_len = max(max_len, right - left + 1)
            else:
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1
                seen.add(s[right])
        return max_len

         

sol = Solution()

print(sol.lengthOfLongestSubstring(s = "abcabcbb")) # 3

print(sol.lengthOfLongestSubstring(s ="cdd")) # 2

print(sol.lengthOfLongestSubstring(s = "bbbbb")) # 1

print(sol.lengthOfLongestSubstring(s = "pwwkew")) # 3 wke

print(sol.lengthOfLongestSubstring("dvdf")) # 3

print(sol.lengthOfLongestSubstring("")) # 0
