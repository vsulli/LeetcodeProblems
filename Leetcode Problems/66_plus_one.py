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
        # loop through array in reverse order adding as you go
        # include + 1 with this sum
        carry = 0
        for i in range(len(digits)-1, -1, -1):
            if i == len(digits) - 1:
                sum = digits[i] + 1
                if sum > 9:
                    digits[i] = sum % 10 # ones place
                    carry = (sum - sum % 10) // 10
                else:
                    digits[i] = sum
                    carry = (sum - sum % 10) // 10
            else:
                sum = digits[i] + carry
                if sum > 9:
                    digits[i] = sum % 10 # next place
                    carry = (sum - sum % 10) // 10
                else:
                    digits[i] = sum
                    carry = (sum - sum % 10) // 10

        if carry: 
            digits.insert(0, digits[i] + carry)
            carry = 0

        return digits
            

sol = Solution()

print(sol.plusOne(digits = [1,2,3]))  # 123 + 1 = 124 [1,2,4]

print(sol.plusOne(digits = [4,3,2,1])) # [4,3,2,2]

print(sol.plusOne(digits = [9])) # [1,0]

print(sol.plusOne(digits = [0])) # [1]

print(sol.plusOne(digits = [8, 9, 9, 9])) # [9, 0, 0, 0]