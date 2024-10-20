
'''
Maximum Count of Positive Integer and Negative Integer
Leetcode #2529
vsulli
20 October 2024

Given an array nums sorted in non-decreasing order, 
return the maximum between the number of positive 
integers and the number of negative integers.

In other words, if the number of positive integers 
in nums is pos and the number of negative integers 
is neg, then return the maximum of pos and neg.
Note that 0 is neither positive nor negative.
'''

from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # array is sorted in non-decreasing order
        # if you get the middle, if middle is negative
            #  set count =  m_idx - l_idx + 1
            # move l = m + 1
        # if you get middle and middle is 0, don't update count but move left pointer right
            # l = m + 1
        # else , middle is pos?
        # once you get to 0, want to advance until left pointer is not 0
        # then you know entire rest of array is pos

        neg_count = 0
        pos_count = 0

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2

            if nums[m] < 0:
                neg_count = m - l + 1
                l = m + 1
            elif nums[m] > 0:
                pos_count = r - m + 1
                l = m - 1
            
            elif nums[m] == 0:
                pass
                # possible that there is another 0 to left...or right
                # advance left pointer until it is no longer 0
                # calculate remaining amount of array  that would be pos
    
        
        return max(pos_count, neg_count)

sol = Solution()

print(sol.maximumCount(nums = [-2,-1,-1,1,2,3])) # 3

print(sol.maximumCount(nums = [-3,-2,-1,0,0,1,2])) # 3

print(sol.maximumCount(nums = [5,20,66,1314])) # 4