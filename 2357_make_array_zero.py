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

class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        operations = 0
        # choose a pos value x <= smallest num in nums
        # subtract that value from every pos element in nums
        # every element needs to equal 0
        while sum(nums[:]) != 0:
            # set min, but not 0
            x = min(n for n in nums if n != 0)
            operations +=1
            for i in range(len(nums)):
                if nums[i] > 0:
                    nums[i] = nums[i] - x
            
        return operations

sol = Solution()

print(sol.minimumOperations(nums = [1,5,0,3,5])) # 3

print(sol.minimumOperations(nums = [0])) # 0 