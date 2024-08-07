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
        # max number 2147483648
        # dictionary with terms for Billion, Million, Thousand, Hundred
        # ninety, eighty, seventy...
        # nine, eight...
        num_word_dict = {1000000000: 'Billion', 1000000: 'Million', 1000: 'Thousand', 100: 'Hundred',
                         90: 'Ninety', 80: 'Eighty', 70: 'Seventy', 60: 'Sixty', 50: 'Fifty', 40: 'Forty', 30: 'Thirty', 20: 'Twenty',
                         19: 'Nineteen', 18: 'Eighteen', 17: 'Seventeen', 16: 'Sixteen', 15: 'Fifteen', 14: 'Fourteen', 13: 'Thirteen',
                         12: 'Twelve', 11: 'Eleven', 10: 'Ten', 9: 'Nine', 8: 'Eight', 7: 'Seven', 6: 'Six', 5: 'Five',
                         4: 'Four', 3: 'Three', 2: 'Two', 1: 'One'}

sol = Solution()
print(sol.numberToWords(num = 123)) 
# "One Hundred Twenty Three"

print(sol.numberToWords(12345)) 
# "Twelve Thousand Three Hundred Forty Five"

print(sol.numberToWords(1234567)) 
# "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
