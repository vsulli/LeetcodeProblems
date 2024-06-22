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
        index = 0
        j = 0
        for i in range(len(haystack)):
            if haystack[i] == needle[j]:
                j+=1
                print(haystack[index:i+1])
                if haystack[index:i+1] == needle:
                    return index
            # if they don't match, then reset index to be current i
            # reset j to be beginning of needle
            else:
                index = i+1
                j = 0

        return -1

sol = Solution()

'''
print(sol.strStr(haystack= "sadbutsad", needle = "sad")) # index 0

print(sol.strStr(haystack="leetcode", needle="leeto")) # -1

print(sol.strStr(haystack="goodcar", needle="car")) # 4

print(sol.strStr(haystack="cargood", needle="car")) # 0
'''
print(sol.strStr(haystack="mississippi", needle="issip")) #4