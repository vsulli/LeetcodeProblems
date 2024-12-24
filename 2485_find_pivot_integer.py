'''
Find the Pivot Integer
Leetcode # 2357
vsulli
23 December 2024

Given a positive integer n, find the 
pivot integer x such that:

The sum of all elements between 1 
and x inclusively equals the sum of 
all elements between x and n inclusively.
Return the pivot integer x. If no such 
integer exists, return -1. It is guaranteed 
that there will be at most one pivot index 
for the given input.

'''

class Solution:
    def pivotInteger(self, n: int) -> int:
        # Initialize left and right pointers for binary search
        left, right = 1, n
        
        # Calculate the total sum of the sequence
        total_sum = n * (n + 1) // 2

        # Binary search for the pivot point
        while left < right:
            # Calculate the mid-point
            mid = (left + right) // 2

            # Check if the difference between the square of mid and the total sum is negative
            if mid * mid - total_sum < 0:
                left = mid + 1  # Adjust the left bound if the sum is smaller
            else:
                right = mid  # Adjust the right bound if the sum is equal or greater

        # Check if the square of the left pointer minus the total sum is zero
        if left * left - total_sum == 0:
            return left
        else:
            return -1

sol =  Solution()

print(sol.pivotInteger(n = 8)) # 6

print(sol.pivotInteger(n = 1)) # 1

print(sol.pivotInteger(n = 4)) # -1