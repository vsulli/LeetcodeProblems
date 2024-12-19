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
        # array contains numbers from 0 - (length of array - 1)
        # want to know how many splits you can have where after you sort those chunks
        # the concatenated result matches the sorted array
        # start with as many chunks as possible and reduce?
        # 10 is largest number of n
        chunks = 1
        p = 1
        sorted_arr = sorted(arr)
        if sorted_arr == arr:
            return len(arr)
        # where to split to put in order?
        # where 2nd pointer is at a value that is greater than first?
        # if rest of array is in order, then you can just count those as individual chunks
        for i in range(len(arr)):
            if arr[p] > arr[i]:
                chunks += 1
            p = i + 1
            

        return chunks

sol = Solution()

print(sol.maxChunksToSorted(arr = [4,3,2,1,0])) # 1

print(sol.maxChunksToSorted(arr = [1,0,2,3,4])) # 4 

print(sol.maxChunksToSorted(arr = [0,1,2,3,4])) # 5

print(sol.maxChunksToSorted(arr = [0,1,2,4,3]))  # 4

