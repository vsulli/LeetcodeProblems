''' 
Construct String With Repeat Limit
Leetcode # 2182
vsulli
17 December 2024

You are given a string s and an integer repeatLimit. 
Construct a new string repeatLimitedString using the 
characters of s such that no letter appears more than 
repeatLimit times in a row. You do not have to use all 
characters from s.

Return the lexicographically largest 
repeatLimitedString possible.

A string a is lexicographically larger 
than a string b if in the first position 
where a and b differ, string a has a 
letter that appears later in the alphabet 
than the corresponding letter in b. If the 
first min(a.length, b.length) characters do 
not differ, then the longer string is the 
lexicographically larger one.
'''

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # to return lexicographically larger string, want later letters to appear later in constructed string
        # but can't have more than limit in a row
        res = ""
        count = 1
        p = 0
        # need to get dictionary of all counts for letters first?
        letter_count = {}
        for l in s:
            if not l in letter_count:
                letter_count[l] = 1
            else:
                letter_count[l] += 1
        print(letter_count)



sol = Solution()

print(sol.repeatLimitedString(s = "cczazcc", repeatLimit = 3))

print(sol.repeatLimitedString(s = "aababab", repeatLimit = 2))

