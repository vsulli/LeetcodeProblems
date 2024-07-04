'''
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

class Solution:
    def reverse(self, x: int) -> int:
        num = abs(x)
        res = 0

        hundreds = (num % 10) * 100

        tens = ((num // 10) % 10) * 10

        ones = ((num // 100) % 10) 

        res = hundreds + tens + ones

        return -res if x < 0 else res


sol = Solution()

print(sol.reverse(x = 123)) 


print(sol.reverse(x = -123))

print(sol.reverse(x = 120))
