'''
Contains Duplicate II
Leetcode # 219
vsulli
11 June 2024

Given an integer array nums and an integer k, 
return true if there are two distinct indices, i and j
in the array such that nums[i] == nums[j] and abs(i - j) <= k
'''

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        pass

sol = Solution()
print(sol.containsNearbyDuplicate(nums = [1,2,3,1], k = 3)) # true

print(sol.containsNearbyDuplicate(nums = [1,0,1,1], k = 1)) # true

print(sol.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2)) # false

