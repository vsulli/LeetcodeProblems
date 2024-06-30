'''
Roman to Integer
Leetcode # 13
vsulli
30 June 2024

Roman numerals are represented by 
seven different symbols: I, V, 
X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in 
Roman numeral, just two ones added 
together. 12 is written as XII, which 
is simply X + II. The number 27 is 
written as XXVII, which is XX + V + II.

Roman numerals are usually written 
largest to smallest from left to right. 
However, the numeral for four is not IIII. 
Instead, the number four is written as IV. 
Because the one is before the five we subtract 
it making four. The same principle applies to 
the number nine, which is written as IX. There 
are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_dict = {"I": 1, "V": 5, "X": 10, "L":50, "C": 100, "D": 500, "M": 1000}
        ans = 0
        # create a dictionary?
        while s != "":
            # 4 and 9
            if "IV" in s:
                ans += 4
                s.replace("IV", "")
            elif "IX" in s:
                ans += 9
                s.replace("IX", "")
            # 40 and 90
            elif "XL" in s:
                ans += 40
                s.replace("XL","")
            elif "XC" in s:
                ans += 90
                s.replace("XC", "")

            # 400 and 900
            elif "CD" in s:
                ans += 400
                s.replace("CD", "")
            elif "CM" in s:
                ans += 900
                s.replace("CM", "")
            else:
                ans += symbol_dict[s[0]]
                s.pop(0)
                print(s)
        return ans


sol = Solution()

print(sol.romanToInt(s = "III")) # 3

print(sol.romanToInt(s = "LVIII")) # 58

print(sol.romanToInt(s = "MCMXCIV")) # 1994