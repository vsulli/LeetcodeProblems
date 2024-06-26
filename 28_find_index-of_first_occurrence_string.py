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
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

sol = Solution()


print(sol.strStr(haystack= "sadbutsad", needle = "sad")) # index 0

print(sol.strStr(haystack="leetcode", needle="leeto")) # -1

print(sol.strStr(haystack="goodcar", needle="car")) # 4

print(sol.strStr(haystack="cargood", needle="car")) # 0

print(sol.strStr(haystack="mississippi", needle="issip")) #4