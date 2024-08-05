''' 
Kth Distinct String in an Array
Leetcode # 2053
vsulli
5 August 2024

A distinct string is a string that 
is present only once in an array.

Given an array of strings arr, and 
an integer k, return the kth distinct 
string present in arr. If there are 
fewer than k distinct strings, return 
an empty string "".

Note that the strings are considered 
in the order in which they appear in 
the array.
'''
from collections import OrderedDict
class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        arr_set = set(arr)

        arr_count = {}
        for l in arr_set:
            if l not in arr_count:
                arr_count[l] = 1
            else:
                arr_count[l] += 1
        print(arr_count)

        i = 1
        for k in arr_count:
            if arr_count.get(k) == 1 and i == k:
                return k
            elif arr_count.get(k) == 1:
                i += 1
        return ""

        
        


sol = Solution()

print(sol.kthDistinct(arr = ["d","b","c","b","c","a"], k = 2)) # d and a only appear once, 
# a is 2nd distinct so "a" is returned

print(sol.kthDistinct(arr = ["aaa","aa","a"], k = 1)) # "aaa"

print(sol.kthDistinct(arr = ["a","b","a"], k = 3)) # "" because there aren't 3 distinct strings