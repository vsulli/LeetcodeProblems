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
        # 1 - 6 will always be that number
        if 1 <= n <= 6:
            return n
        
        # start with 7 
        ugly_num = 7
        count = 6
        
        while count < n:
            print("num: " + str(ugly_num))
            print("count: " + str(count))
            print("-----")
            # has 2, 3, or 5 as a factor
            if ugly_num % 2 == 0 or ugly_num % 3 == 0 or ugly_num % 5 == 0:
                count += 1
 
            ugly_num += 1
            
            
            
        return ugly_num

sol = Solution()

print(sol.nthUglyNumber(n = 10)) # 12 - generate first 10 ugly numbers 

print(sol.nthUglyNumber(n = 2)) # 2

'''

print(sol.nthUglyNumber(n = 1)) # 1
'''