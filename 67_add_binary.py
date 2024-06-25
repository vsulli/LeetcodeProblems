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
        # sum string
        # carry value
        # pointers for string a and b
        res = []
        carry = 0
        i = len(a) - 1
        j = len(b) -1

        # my algo missing carry here
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            res.append(str(carry % 2)) # mod will either return 0 or 2
            carry //= 2 # stores leftover
        return ''.join(reversed(res))
    

sol = Solution()

print(sol.addBinary(a = "11", b = "1")) # 100
print(sol.addBinary(a = "1", b = "11")) # 100

print(sol.addBinary(a = "1010", b = "1011")) # 10101

print(sol.addBinary(a = "0", b = "0")) # 0

print(sol.addBinary(a = "10101010", b = "111")) # 10110001

print(sol.addBinary(a = "1111", b = "1111")) # "11110"