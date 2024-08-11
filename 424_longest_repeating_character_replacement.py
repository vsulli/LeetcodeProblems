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
        # start with left pointer and right pointer
        # get counts of all letters?
        # for new string that can be built - go to character that occurs most often?
        freq_dic = {}

        pointer = 1
        new_string = ""
        for c in s:
            if c in freq_dic:
                freq_dic[c] += 1
            else:
                freq_dic[c] = 1
        
        print(freq_dic)

sol = Solution()

print(sol.characterReplacement(s = "ABAB", k = 2))
# 4 - replace either 2 A's or 2 B's

print(sol.characterReplacement(s = "AABABBA", k = 1))
# 4 - replace one A in the middle to B