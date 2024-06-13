'''
Valid Anagram
Leetcode #242
vsulli
12 June 2024

Given two strings s and t, return true if t is an 
anagram of s, and false otherwise

An anagram is a word or phrase formed by rearranging the letters of a 
different word or phrase, typically using all the original letters
exactly once
'''

class Solution:
    def isAnagram(self, s: str, t: str)-> bool:
        if len(s) != len(t):
            return False
        dict_s = {}
        dict_t = {}
        # count of letters in s must match count of letters in t
        for l in s:
            dict_s[l] = dict_s.get(l, 0) + 1
        for l in t:
            dict_t[l] = dict_t.get(l, 0) + 1
        # loop through longer dictionary and check count of each?
        for key in dict_s:
            if dict_s.get(key) != dict_t.get(key):
                return False
        return True
        


sol = Solution()

print(sol.isAnagram(s = "aacc", t = "ccac")) # false

print(sol.isAnagram(s = "anagram", t = "nagaram")) # true

print(sol.isAnagram(s = "rat", t = "car")) # false
