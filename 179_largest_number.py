# TODO read up on greedy algorithm
# read up on cmp_to_key
'''
Largest Number
Leetcode # 179
vsulli
18 September 2024

Given a list of non-negative integers 
nums, arrange them such that they form 
the largest number and return it.

Since the result may be very large, 
so you need to return a string instead 
of an integer.

'''

from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # greedy algorithm
        # sorting - nlogn
        for i, n in enumerate(nums):
            nums[i] = str(n)


        # our custom comparison function
        # compares two numbers and used as key to sort
        def compare(n1, n2):
            # n1 goes first
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1

        nums = sorted(nums, key=cmp_to_key(compare))

        return str(int("".join(nums))) # adds list of strings together
        # converting to int gets rid of "000" problem




sol = Solution()

print(sol.largestNumber(nums = [10,2]))

print(sol.largestNumber(nums = [3,30,34,5,9]))

