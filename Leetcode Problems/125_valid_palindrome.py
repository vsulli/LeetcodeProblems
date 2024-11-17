'''
Valid Palindrome
Leetcode # 125
vsulli
22 June 2024

A phrase is a palindrome if, after converting all 
uppercase letters into lowercase letters and 
removing all non-alphanumeric characters, it 
reads the same forward and backward. Alphanumeric 
characters include letters and numbers.

Given a string s, return true if it is a palindrome, 
or false otherwise.
'''

import string


class Solution:
    def alphaNum(self, c):
        # check if ascii value falls within range for upper letter,
        # lower letter, or number
        return (ord('A') <= (ord(c)) <= ord('Z') or
                ord('a') <= (ord(c)) <= ord('z') or
                ord('0') <= (ord(c)) <= ord('9'))

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        # while pointers haven't met
        while l < r:
            # increment left pointer if necessary and make sure doesn't
            # pass right pointer
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -=1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True



sol = Solution()

print(sol.isPalindrome(s = "A man, a plan, a canal: Panama")) # true

print(sol.isPalindrome(s = "race a car")) # false

print(sol.isPalindrome(s = " ")) # true

