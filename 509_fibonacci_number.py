'''
Fibonacci Number
Leetcode # 509
vsulli
18 July 2024

The Fibonacci numbers, commonly denoted 
F(n) form a sequence, called the 
Fibonacci sequence, such that each 
number is the sum of the two preceding 
ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
'''

class Solution:



    dp = [-1] * 31
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        # Temporary variables to store values of fib(n-1) & fib(n-2)
        first = self.dp[n - 1] if self.dp[n - 1] != -1 else self.fib(n - 1)
        second = self.dp[n - 2] if self.dp[n - 2] != -1 else self.fib(n - 2)

        # Memoization
        self.dp[n] = first + second
        return self.dp[n]
    


sol = Solution()

print(sol.fib(n = 2)) # 1

print(sol.fib(n = 3)) # 2

print(sol.fib(n = 4)) # 3