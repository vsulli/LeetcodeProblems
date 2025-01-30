#238 product of array except self

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int])-> List[int]:
        answer  = [1] * len(nums) 

        prefix = 1
        #go from left
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]

        # go from right
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= postfix 
            postfix *= nums[i]

        return answer