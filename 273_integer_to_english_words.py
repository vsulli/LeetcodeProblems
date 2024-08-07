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
        pass

sol = Solution()
print(sol.numberToWords(num = 123)) 
# "One Hundred Twenty Three"

print(sol.numberToWords(12345)) 
# "Twelve Thousand Three Hundred Forty Five"

print(sol.numberToWords(1234567)) 
# "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
