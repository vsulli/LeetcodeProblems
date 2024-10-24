
'''
69 - Sqrt(x)
Given a non-negative integer x, return the square 
root of x rounded down to the nearest integer. The 
returned integer should be non-negative as well.

You must not use any built-in exponent function or 
operator.

For example, do not use pow(x, 0.5) in c++ or x ** 
0.5 in python.
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        # try all numbers in a range to find the number that would be its square?
        for i in range(0, 2147483648):
            if i * i == x:
                return i
            elif i * i > x:
                return i - 1

sol = Solution()



print(sol.mySqrt(x = 4)) # 2


print(sol.mySqrt(x = 8)) # 2

