''' 
Ugly Number II
Leetcode # 264
vsulli
18 August 2024

An ugly number is a positive integer 
whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.
'''


import heapq


class Solution:

    def nthUglyNumber(self, n: int) -> int:
        minHeap = [1]
        visit = set()

        factors = [2, 3, 5]
        for i in range(n):
            num = heapq.heappop(minHeap)
            if i == n - 1:
                return num
            for f in factors:
                if num * f not in visit:
                    visit.add(num * f)
                    heapq.heappush(minHeap, num * f)
                
        

sol = Solution()

print(sol.nthUglyNumber(n = 10)) # 12 - generate first 10 ugly numbers 

print(sol.nthUglyNumber(n = 2)) # 2

print(sol.nthUglyNumber(n = 1)) # 1

print(sol.nthUglyNumber(n = 7)) # 8

print(sol.nthUglyNumber(n = 11)) # 15 
# currently giving 14 because my program currently doesn't get rid of other prime factors 
# 14's prime factors - 1,2, 7, and 14 - can't have 7 as another prime factor
