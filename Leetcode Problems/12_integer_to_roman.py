'''
# TODO Attempting
Integer to Roman
Leetcode # 12
vsulli
2 July 2024

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
        roman_nums = {1: "I",4 : "IV",  5: "V", 9: "IX", 
                      10: "X", 40: "XL", 50: "L", 90: "XC", 
                      100: "C", 400: "CD", 500: "D", 900: 
                      "CM", 1000: "M"}
        res = ""

        # formed by appending conversion of decimal place values from highest to
        # lowest

        # if value doesn't start with 4 or 9
        # select symbol of max value that can be subtracted from the input
        # append it to result
        # subtract its value 
        # convert rest to roman number

        # need to look at number by place

        # ones
        # tens
        # hundreds
        # thousands

        while num != 0:
            # while num isn't 0, mod in order?
            if num % 1000 == 0:
                res = res + ("M" * (num // 1000))
                num -=  1000 * (num // 1000)
            if num % 500 == 0:
                res = res + ("D" * (num // 500))
                num -= 500 * (num // 500)
            if num % 100 == 0:
                res = res + ("C" * (num // 100))
                num -= 100 * (num // 100)
            if num % 50 == 0:    
                print("here")
                res = res + ("L" * (num // 50))
                num -= 50 * (num // 50)
            if num % 10 == 0:    
                res = res + ("X" * (num // 10))
                num -= 10 * (num // 10)
            if num % 5 == 0:    
                res = res + ("V" * (num // 5))
                num -= 5 * (num // 5)
            else:
                res = res + ("I" * num)
                num -= num

        return res


sol = Solution()


'''
print(sol.intToRoman(num = 1))
print(sol.intToRoman(num = 10))
print(sol.intToRoman(num = 1000))
'''
print(sol.intToRoman(58)) # "LVIII"


'''
print(sol.intToRoman(num = 3749)) # "MMMDCCXLIX"

print(sol.intToRoman(58)) # "LVIII"

print(sol.intToRoman(1994)) # "MCMXCIV"

'''