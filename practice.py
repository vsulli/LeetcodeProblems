# 238 Product of Array Except SElf

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # loop through twice
        # get product from left and then product from right
        output = [1] * len(nums)
        
        left = 1
        for i in range(len(nums)):
            output[i] *= left
            left *= nums[i]
        
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= right
            right *= nums[i]
    
        return output        


sol = Solution()
print(sol.productExceptSelf(nums = [1,2,3,4]))

print(sol.productExceptSelf(nums = [-1, 1, 0, -3, 3]))