# TODO - need different way to loop through string
'''
Find the Index of the First Occurrence in a String
Leetcode # 28
vsulli
20 June 2024

Given two strings needle and haystack, return 
the index of the first occurrence of needle in haystack, or -1
if needle is not part of haystack
'''

class Solution:
    def strStr(self, haystack: str, needle: str)-> int:
        # return index of start of the word
        
        # loop through whole string
        # if you encounter first letter of needle, store index
        # if you loop through entire part of string and all letters there
        # return index
        # else keep looking for word in rest of str
        return haystack.find(needle)

sol = Solution()

'''
print(sol.strStr(haystack= "sadbutsad", needle = "sad")) # index 0

print(sol.strStr(haystack="leetcode", needle="leeto")) # -1

print(sol.strStr(haystack="goodcar", needle="car")) # 4

print(sol.strStr(haystack="cargood", needle="car")) # 0
'''
print(sol.strStr(haystack="mississippi", needle="issip")) #4