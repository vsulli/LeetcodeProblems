'''
Sliding Window Maximum
Leetcode # 239
vsulli
5 September 2024

You are given an array of integers nums, 
there is a sliding window of size k 
which is moving from the very left 
of the array to the very right. 
You can only see the k numbers in 
the window. Each time the sliding 
window moves right by one position.

Return the max sliding window.
'''

from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # need a different way to calculate new max? compare to last?
        output = []
        l = 1
        currMax = max(nums[0:k])
        output.append(currMax)
        for r in range(k, len(nums)):
            # need to see if nums[r] is greater than currMax, if so then that gets appended
            # and becomes new currMax
            # also matters position of max in the subarray
            if nums[r] > currMax:
                currMax = nums[r]
            output.append(currMax)
            l+= 1

        return output

sol = Solution()


print(sol.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3)) # [3,3,5,5,6,7]

print(sol.maxSlidingWindow(nums = [1], k = 1)) # [1]

print(sol.maxSlidingWindow(nums = [1,3,1,2,0,5], k = 3)) # [3, 3, 2, 5]