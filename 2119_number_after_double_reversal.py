'''
Reverse Integer
Leetcode # 2119
vsulli
4 July 2024

Reversing an integer means to reverse all its digits.

For example, reversing 2021 gives 1202. Reversing 12300 gives 321 as the leading zeros are not retained.
Given an integer num, reverse num to get reversed1, then reverse reversed1 to get reversed2. Return true if reversed2 equals num. Otherwise return false.
'''
import math
class Solution:
    def reverseNum(self, num) -> int:
        rev = 0
        # take right-most digit
        while num != 0:
            digit = num % 10 if num > 0 else num % -10

            rev = rev * 10 + digit

            num = math.trunc( num / 10)
        return rev
    
    def isSameAfterReversals(self, num: int) -> bool:
        reversed1  = self.reverseNum(num)
        reversed2 = self.reverseNum(reversed1)
        return reversed2 == num


sol = Solution()

print(sol.isSameAfterReversals(num = 526)) # true

print(sol.isSameAfterReversals(num = 1800)) # false