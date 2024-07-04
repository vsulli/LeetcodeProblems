'''
# TODO WIP
Reverse Integer
Leetcode # 7
vsulli
3 July 2024

Given a signed 32-bit integer x,
return x with its digits reversed
If reversing x causes the value to go outside
the signed 32-bit integer range [-2^31, 2^31 - 1] then return 0

assume the environment doesn't allow you to store
64 bit integers  signed or unsigned
'''

import math

class Solution:
    def reverse(self, x: int) -> int:

        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31
        reverse = 0

        while x != 0:
            # causes value to go outside range return 0
            if reverse > MAX_INT / 10 or reverse < MIN_INT / 10:
                return 0
            
            digit = x % 10 if x > 0 else x % -10
            reverse = reverse * 10 + digit
            x = math.trunc(x / 10)

        return reverse


sol = Solution()


print(sol.reverse(x = 123)) 

print(sol.reverse(x = -123))

print(sol.reverse(x = 120))

print(sol.reverse(x = 1))

print(sol.reverse(x = 75))
