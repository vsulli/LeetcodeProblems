# Daily Practice Sheet for use with ANKI

class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        
        # two pointers?
        total = 0
        # have to check if they are divisible by k

        for i in range(len(nums)):
            total = nums[i]
            for j in range(i+1,len(nums)):
                total += nums[j]
                if total %  k == 0:
                    return True
            total = 0
                
        return False

sol = Solution()

print(sol.checkSubarraySum(nums = [23,2,4,6,7], k = 6)) # true

print(sol.checkSubarraySum(nums = [23,2,6,4,7], k = 6)) # true

print(sol.checkSubarraySum(nums = [23,2,6,4,7], k = 13)) # false