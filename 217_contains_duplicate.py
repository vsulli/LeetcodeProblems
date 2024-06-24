'''
Contains Duplicate
Leetcode # 217
vsulli
10 June 2024

Given an integer array nums, return true
if any value appears at least twice in the array,
and return false if every element is distinct. 
'''

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # set loop until you encounter duplicate
        # O(n) at most
        seen = {}
        for num in nums:
            if num in seen and seen[num] >= 1:
                return True
            seen[num] = seen.get(num, 0) + 1
        return False

sol = Solution()
print(sol.containsDuplicate(nums = [1,2,3,1])) # true

print(sol.containsDuplicate(nums = [1,2,3,4])) # false

print(sol.containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2])) # true