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

import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # use deque for O(n) solution
        # always decreasing in deque
        # monotonically decreasing queue
        output = []
        l = r = 0
        q = collections.deque() # indices

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left val from window if out of  bounds
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1

            r += 1

        return output
        

sol = Solution()


print(sol.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3)) # [3,3,5,5,6,7]

print(sol.maxSlidingWindow(nums = [1], k = 1)) # [1]

print(sol.maxSlidingWindow(nums = [1,3,1,2,0,5], k = 3)) # [3, 3, 2, 5]