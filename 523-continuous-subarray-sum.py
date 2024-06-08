'''
Continuous Subarray Sum
Leetcode # 523
# vsulli
# 8 June 2024

Given an integer array nums and an integer k, return true if nums 
has a good subarray or false otherwise.

* subarray length >= 2
* sum of elements multiple of k
'''


class Solution:
    def checkSubarraySum(self, nums: list[int], k: int)-> bool:
        remainder = {0: -1}
        total = 0

            
        for i, n in enumerate(nums):
            total += n
            r = total % k

            # remainder not in hashmap
            if r not in remainder:
                remainder[r] = i
            # remainder in hashmap
            elif i - remainder[r] > 1:
                return True

        return False

sol = Solution()

print(sol.checkSubarraySum(nums = [1, 0], k = 2))
'''
print(sol.checkSubarraySum(nums = [23,2,4,6,7], k = 6)) # true

print(sol.checkSubarraySum(nums = [23,2,6,4,7], k = 6)) # true

print(sol.checkSubarraySum(nums = [23,2,6,4,7], k = 13)) # false

'''