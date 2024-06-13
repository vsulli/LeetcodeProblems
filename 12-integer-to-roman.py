'''
Integer to Roman
Leetcode # 12
vsulli
12 June 2024

Seven different symbols reprsent Roman numerals 
with the following values

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

Given an integer, convert it to a Roman numeral
'''

class Solution:
    def intToRoman(self, num: int)-> str:
        roman_nums = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        res = ""
        while num != 0:
            # while num isn't 0, mod in order?
            if num % 1000 == 0:
                res = res + ("M" * (num // 1000))
                num -= num * (num // 1000)
            if num % 500 == 0:
                res = res + ("D" * (num // 500))
                num -= num * (num // 500)
            if num % 100 == 0:
                res = res + ("C" * (num // 100))
                num -= num * (num // 100)
            if num % 50 == 0:    
                res = res + ("L" * (num // 50))
                num -= num * (num // 50)
            if num % 10 == 0:    
                res = res + ("X" * (num // 10))
                num -= num * (num // 10)
            if num % 5 == 0:    
                res = res + ("V" * (num // 5))
                num -= num * (num // 5)
            if num % 1 == 0:    
                res = res + ("I" * (num // 1))
                num -= num * (num // 1)

        return res


sol = Solution()

print(sol.intToRoman(num = 1))
print(sol.intToRoman(num = 10))
print(sol.intToRoman(num = 1000))
'''
print(sol.intToRoman(num = 3749)) # "MMMDCCXLIX"

print(sol.intToRoman(58)) # "LVIII"

print(sol.intToRoman(1994)) # "MCMXCIV"

'''