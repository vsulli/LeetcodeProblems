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
        nums = [1]
        i2, i3, i5 = 0, 0 , 0

        for i in range(1, n):
            next_num = min(
            nums[i2] * 2, nums[i3] * 3, nums[i5] * 5
            )
            nums.append(next_num)
            if next_num == nums[i2] * 2:
                i2 += 1
            if next_num == nums[i3] * 3:
                i3 += 1
            if next_num == nums[i5] * 5:
                i5 += 1

        return nums[n - 1]
                
        

sol = Solution()

print(sol.nthUglyNumber(n = 10)) # 12 - generate first 10 ugly numbers 

print(sol.nthUglyNumber(n = 2)) # 2

print(sol.nthUglyNumber(n = 1)) # 1

print(sol.nthUglyNumber(n = 7)) # 8

print(sol.nthUglyNumber(n = 11)) # 15 
# currently giving 14 because my program currently doesn't get rid of other prime factors 
# 14's prime factors - 1,2, 7, and 14 - can't have 7 as another prime factor
