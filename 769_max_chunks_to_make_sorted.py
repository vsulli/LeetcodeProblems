''' 
Max Chunks to Make Sorted
Leetcode # 769
vsulli
19 December 2024

You are given an integer array arr of 
length n that represents a permutation 
of the integers in the range [0, n - 1].

We split arr into some number of chunks 
(i.e., partitions), and individually sort 
each chunk. After concatenating them, the 
result should equal the sorted array.

Return the largest number of chunks we can 
make to sort the array.
'''
from typing import List
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

sol = Solution()

print(sol.maxChunksToSorted(arr = [4,3,2,1,0]))

print(sol.maxChunksToSorted(arr = [1,0,2,3,4]))