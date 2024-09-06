# leetcode 239 
# sliding window maximum

import collections

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        output = []
        q = collections.deque() # stores indices
        l = r = 0


        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

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
