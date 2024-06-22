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
    def isPalindrome(self, s: str) -> bool:
        # get rid of punctuation and spaces
        # check beginning and end with two pointers
        s = s.translate(str.maketrans('', '', string.punctuation))
        print(s)
        
sol = Solution()

print(sol.isPalindrome(s = "A man, a plan, a canal: Panama")) # true

print(sol.isPalindrome(s = "race a car"))

print(sol.isPalindrome(s = " ")) # true

