'''
Plus One
Leetcode # 66
vsulli
23 June 2024

You are given a large integer
represented as an integer array digits,
where each digits[i] is the ith digit of the integer
The digits are ordered from most significant to least 
significant in left-to-right order. The large integer does not
contain any leading 0's

Increment the large integer by one and return the resulting array of digits

'''

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        pass
        # loop through array in reverse order adding as you go
        # include + 1 with this sum

sol = Solution()

print(sol.plusOne(digits = [1,2,3]))  # 123 + 1 = 124 [1,2,4]

print(sol.plusOne(digits = [4,3,2,1])) # [4,3,2,2]

print(sol.plusOne(digits = [9])) [1,0]