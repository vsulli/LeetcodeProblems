
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
        if x == 0:
            return 0
        elif x == 1:
            return 1
        
        count = 1

        # while 2^count <= x increase it
        # once it gets over, return previous count?
        while (2 ** count) < x:
            count += 1
        

        return count


sol = Solution()

'''

print(sol.mySqrt(x = 4)) # 2
'''

print(sol.mySqrt(x = 8)) # 2

