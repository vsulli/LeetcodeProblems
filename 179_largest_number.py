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

from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # out of all single length ones compared to first digit - in order

        # does it still matter to sort it?
        nums.sort(reverse=True)
        res = str(nums[0]) # initialize result to first number
        print(nums)
        # build string and then as you go through in O(n) time insert next number? - try leftmost to make biggest?
        
        # loop through remainder of list
        for i in range(1, len(nums)):
            # new number before > new number after
            # compare it to the first digit?
            # how to keep track of numbers that are more than one digit but already placed in string?
            if int(str(nums[i])+res) > int(res+str(nums[i])):
                res = str(nums[i]) + res
            else:
                res = res + str(nums[i])
            print(res)
        return res



sol = Solution()
'''
print(sol.largestNumber(nums = [10,2]))

'''

print(sol.largestNumber(nums = [3,30,34,5,9]))

