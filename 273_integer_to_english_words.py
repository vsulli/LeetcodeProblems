''' 
Integer to English Words
Leetcode # 273
vsulli
6 August 2024

Convert a non-negative integer 
num to its English words representation.
'''

class Solution:

    def numberToWords(self, num: int) -> str:
        # base case of 0
        if num == 0:
            return "Zero"
        
        # two hashmaps
        # 1-19
        ones_map = {
            1: "One",
            2: "Two",
            3: 'Three', 
            4: 'Four', 
            5: 'Five', 
            6: 'Six', 
            7: 'Seven', 
            8: 'Eight', 
            9: 'Nine',
            10: 'Ten', 
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
        }

        tens_map = {
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty", 
            90: "Ninety",
        }

        # converts digits into a string
        def get_string(n):
            return
        
        postfix = ["", " Thousand", " Million", " Billion"] # include space
        i = 0 # tells you what your postfix will be 
        res = []

        while num:
            # get last 3 digits
            digits = num % 1000
            s = get_string(digits) + postfix[i]
            if s:
               res = [s] + res 
            # remove the digits from num by dividing
            num //= 1000

        return " ".join(res)




sol = Solution()

print(sol.numberToWords(37))

'''
print(sol.numberToWords(num = 123)) 
# "One Hundred Twenty Three"
# 3 digits

print(sol.numberToWords(12345)) 
# "Twelve Thousand Three Hundred Forty Five"
# 5 digits

print(sol.numberToWords(1234567)) 
# "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
# 7 digits
'''