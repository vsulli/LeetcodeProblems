''' 
Check if a Number is a Sum of Powers
of Three
vsulli
3 March 2025

Given an integer n, return true if it 
is possible to represent n as the sum of 
distinct powers of three. Otherwise, return 
false.

An integer y is a power of three if there 
exists an integer x such that y == 3x.

 
'''

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        distinct_powers = False
        sum =  0
        while sum != n:
            # 12 / 3 = 4
            # 91 / 3 = 30.3 -> 90/3 = 30 + 1/3 remainder of 1 can be represented as 3^0
            # 21 / 3 = 
            # remove the 1?

        return distinct_powers

sol = Solution()

print(sol.checkPowersOfThree(n = 12))

print(sol.checkPowersOfThree(n = 91))

print(sol.checkPowersOfThree(n = 21))