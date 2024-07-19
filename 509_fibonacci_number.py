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
    def fib(self, n: int) -> int:
        # each number is the sum of the two before it
        f0 = 0
        f1 = 1
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        sum = 0

        for i in range(2, n+1):
            sum 

sol = Solution()

print(sol.fib(n = 2)) # 1

print(sol.fib(n = 3)) # 2

print(sol.fib(n = 4)) # 3