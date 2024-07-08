'''
Make Array Zero by
Subtracking Equal Amounts
Leetcode # 2357
vsulli
7 July 2024

You are given a non-negative integer 
array nums. In one operation, you must:

Choose a positive integer x such that 
x is less than or equal to the smallest 
non-zero element in nums.
Subtract x from every positive element 
in nums.
Return the minimum number of operations 
to make every element in nums equal to 0.

'''
import heapq

class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        # only care about unique positive numbers in the array
        # total number of operations is # unique pos numbers
        # since each operation can reduce the array by one of these numbers
        # min heap
        # O(n^2 log n) time
        # O(1) space
        heapq.heapify(nums)
        operations = 0

        while nums:
            x = heapq.heappop(nums)
            if x == 0:
                continue
            else:
                for i in range(len(nums)):
                    nums[i] -= x
                operations += 1

        return operations
        

sol = Solution()

print(sol.minimumOperations(nums = [1,5,0,3,5])) # 3

print(sol.minimumOperations(nums = [0])) # 0 