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
        num_word_dict = {1000000000: 'Billion', 1000000: 'Million', 1000000: 'Hundred Thousand', 10000: 'Ten Thousand', 1000: 'Thousand', 100: 'Hundred',
                         90: 'Ninety', 80: 'Eighty', 70: 'Seventy', 60: 'Sixty', 50: 'Fifty', 40: 'Forty', 30: 'Thirty', 20: 'Twenty',
                         19: 'Nineteen', 18: 'Eighteen', 17: 'Seventeen', 16: 'Sixteen', 15: 'Fifteen', 14: 'Fourteen', 13: 'Thirteen',
                         12: 'Twelve', 11: 'Eleven', 10: 'Ten', 9: 'Nine', 8: 'Eight', 7: 'Seven', 6: 'Six', 5: 'Five',
                         4: 'Four', 3: 'Three', 2: 'Two', 1: 'One', 0: 'Zero'}
        
        # get total number of digits to know if starting with Billions, Millions, etc?
        digits_len = len(str(num))
        print(digits_len)

        match digits_len:
            # One Digit - return result from dictionary
            case 1:
                return num_word_dict[num]
            # Hundred 2
            case 2:
                # need to get left-most number for hundred (1-9) + Hundred
                # get 10s (10-90)
                # get 1s if zero? -(1 -9)
                pass
            # Thousands 3
            case 3:
                pass
            case 4: 
                pass
            # Hundred Thousands 5
            case 5: 
                pass
            # Millions will have 6
            case 6:
                pass
            # Billions will have 9 digits to right
            case 9: 
                pass

    


sol = Solution()

print(sol.numberToWords(0))

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