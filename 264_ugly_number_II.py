''' 
Ugly Number II
Leetcode # 264
vsulli
18 August 2024

An ugly number is a positive integer 
whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.
'''
from functools import reduce

class Solution:
    def factors(n):    
        return set(reduce(list.__add__, 
                    ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

    def nthUglyNumber(self, n: int) -> int:
        # 1 - 6 will always be that number
        if 1 <= n <= 6:
            return n
        
        # start with 7 
        ugly_num = 6
        count = 6
        
        while True:
            print("num: " + str(ugly_num))
            print("count: " + str(count))
            print("-----")
            # has 2, 3, or 5 as a factor
            current_factors = self.factors(ugly_num)
            if count == n:
                return ugly_num
            elif 2 in current_factors or 3 in current_factors or 5 in current_factors and len(current_factors == 3):
                count += 1
            
            ugly_num += 1
            
        

sol = Solution()

print(sol.nthUglyNumber(n = 10)) # 12 - generate first 10 ugly numbers 

print(sol.nthUglyNumber(n = 2)) # 2

print(sol.nthUglyNumber(n = 1)) # 1

print(sol.nthUglyNumber(n = 7)) # 8

print(sol.nthUglyNumber(n = 11)) # 15 
# currently giving 14 because my program currently doesn't get rid of other prime factors 
# 14's prime factors - 1,2, 7, and 14 - can't have 7 as another prime factor
