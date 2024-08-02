'''
Find the Duplicate Number
Leetcode # 2678
vsulli
2 August 2024

Given an array of integers nums 
containing n + 1 integers where 
each integer is in the range 
[1, n] inclusive.

There is only one repeated number 
in nums, return this repeated number.

You must solve the problem without 
modifying the array nums and uses 
only constant extra space.

'''

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return fast

        

sol = Solution()

print(sol.findDuplicate(nums = [1,3,4,2,2])) # 2

print(sol.findDuplicate(nums = [3,1,3,4,2])) # 3

print(sol.findDuplicate(nums = [3,3,3,3,3])) # 3
