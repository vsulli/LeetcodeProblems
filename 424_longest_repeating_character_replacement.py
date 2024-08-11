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
# TODO - WIP
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lp = 0
        rp = 1
        count = 0
        n_count = 0
        change = 0

        while rp < len(s):
            while rp < len(s) and s[lp] == s[rp] or change < k:
                if s[rp] != s[lp] and change < k:
                    # s[rp] = s[lp]
                    change += 1
                    n_count +=1
                    rp += 1
                else:
                    n_count += 1
                    rp += 1

            count = max(count, n_count)
            lp = rp
            rp += 1

        return count
            

sol = Solution()

print(sol.characterReplacement(s = "ABAB", k = 2))
# 4 - replace either 2 A's or 2 B's

print(sol.characterReplacement(s = "AABABBA", k = 1))
# 4 - replace one A in the middle to B