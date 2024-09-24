'''
Find the Length of the Longest Common Prefix
Leetcode # 3043
vsulli
24 September 2024

You are given two arrays with positive 
integers arr1 and arr2.

A prefix of a positive integer is an 
integer formed by one or more of its digits, 
starting from its leftmost digit. For example, 
123 is a prefix of the integer 12345, while 234 is not.

A common prefix of two integers a and b is an 
integer c, such that c is a prefix of both a and b. 
For example, 5655359 and 56554 have a common prefix 
565 while 1223 and 43456 do not have a common prefix.

You need to find the length of the longest common 
prefix between all pairs of integers (x, y) such that 
x belongs to arr1 and y belongs to arr2.

Return the length of the longest common prefix among 
all pairs. If no common prefix exists among them, return 0.
'''

from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # need to find prefix from both arr1 and arr2
        # sort?
        # start with leftmost digit of first number in arr1
        # check if firstmost of arr2 matches?

        #  first digit = number // (10 ** (len(str(number)) - 1))

        # are arrays already sorted?
        arr1.sort()
        arr2.sort()

        res = 0
        p2 = 0

        for i in range(len(arr1)):
            # if first number digit matches first digit of 2nd arr
            fd_arr1 = arr1[i] // (10 ** (len(str(arr1[i])) - 1))
            fd_arr2 = arr2[p2] // (10 ** (len(str(arr2[p2])) - 1))
            while fd_arr1 == fd_arr2:
                res += fd_arr1


        return res

sol = Solution()

print(sol.longestCommonPrefix(arr1 = [1,10,100], arr2 = [1000])) # 3 
# 100

print(sol.longestCommonPrefix(arr1 = [1,2,3], arr2 = [4,4,4])) # 0
