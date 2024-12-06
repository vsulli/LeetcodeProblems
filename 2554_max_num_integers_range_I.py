'''
Maximum Number of Integers 
to Choose From a Range I
Leetcode # 2554
vsulli
6 December 2024

You are given an integer 
array banned and two integers 
n and maxSum. You are choosing 
some number of integers following 
the below rules:

The chosen integers have to be 
in the range [1, n].
Each integer can be chosen at 
most once.
The chosen integers should not 
be in the array banned.
The sum of the chosen integers 
should not exceed maxSum.
Return the maximum number of 
integers you can choose following 
the mentioned rules.
'''

from typing import List

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        pass

sol = Solution()

print(sol.maxCount(banned = [1,6,5], n = 5, maxSum = 6))

print(sol.maxCount(banned = [1,2,3,4,5,6,7], n = 8, maxSum = 1))

print(sol.maxCount(banned = [11], n = 7, maxSum = 50))