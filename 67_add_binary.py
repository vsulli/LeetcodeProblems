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
        # list
        res = ""
        ia = len(a) - 1
        ib = len(b) - 1
        valA = 0
        valB = 0
        carry = 0
        sum = 0

        while ia > -1 or ib > -1:
            if a[ia]:
                valA = int(a[ia])
                ia -= 1
            if b[ib]:
                valB = int(b[ib])
                ib -= 1
            sum = valA + valB + carry
            if sum <= 1:
                res = str(sum) + res
                # res.insert(0, sum)
                carry = 0
            else: 
                res = "0" + res
                # res.insert(0, 0)
                carry = 1

        if carry:
            res =  str(carry) + res
            # res.insert(0, carry)
            carry = 0

        # sum = 0,1 - just add to stack
        # sum = 2 - add 0 to stack, 1 to carry
        return res
    

sol = Solution()

print(sol.addBinary(a = "11", b = "1")) # 100

print(sol.addBinary(a = "1010", b = "1011")) # 10101

print(sol.addBinary(a = "0", b = "0")) # 0