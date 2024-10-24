
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
import math

class Solution:
    def mySqrt(self, x: int) -> int:
        return int(math.sqrt(x))

sol = Solution()



print(sol.mySqrt(x = 4)) # 2


print(sol.mySqrt(x = 8)) # 2

