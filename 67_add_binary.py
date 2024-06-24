'''
Add Binary
Leetcode # 67
vsulli
24 June 2024

Given two binary strings a and b,
return their sum as a binary string
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # when adding binary
        # 1+1 = 10
        # 0 + 1 = 1
        # loop through all numbers backwards
        # while there are digits on either one?
        res = []
        ia = len(a) - 1
        ib = len(b) - 1
        valA = 0
        valB = 0
        carry = 0
        sum = 0

        while ia or ib > -1:
            valA = 0
            valB = 0
            if a[ia]:
                valA = a[ia]
            if b[ib]:
                valB = b[ia]
            sum = valA + valB + carry
            if 
                res.insert(0, sum)
            # get a val
            # get b val
            # add carry if it exists

            # decrement a index
            # decrement b index

        return sum
    

sol = Solution()

print(sol.addBinary(a = "11", b = "1")) # 100

print(sol.addBinary(a = "1010", b = "1011")) # 10101