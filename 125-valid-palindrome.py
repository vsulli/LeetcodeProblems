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
        s = s.translate(str.maketrans('', '', string.punctuation + " "))
        # convert string to lowercase
        s = s.lower()
        # check beginning and end with two pointers
        j = len(s) - 1
        for i in range((len(s) // 2)):
            if s[i] != s[j]:
                return False
            j-=1
        return True

sol = Solution()

print(sol.isPalindrome(s = "A man, a plan, a canal: Panama")) # true

print(sol.isPalindrome(s = "race a car")) # false

print(sol.isPalindrome(s = " ")) # true

