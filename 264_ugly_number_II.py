''' 
Ugly Number II
Leetcode # 264
vsulli
18 August 2024

An ugly number is a positive integer 
whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.
'''

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_num = 1
        count = 1

        while count != n:
            # has 2, 3, or 5 as a factor
            if ugly_num % 2 == 0 or ugly_num % 3 == 0 or ugly_num % 5 == 0:
                count += 1
                ugly_num += 1
            else: 
                ugly_num += 1
            
        return ugly_num

sol = Solution()

print(sol.nthUglyNumber(n = 10)) # 12 - generate first 10 ugly numbers 

print(sol.nthUglyNumber(n = 1)) # 1
