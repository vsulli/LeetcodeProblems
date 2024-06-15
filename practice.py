# Daily Practice Sheet for use with ANKI

class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        remainder_map = {0: -1}
        cumulative_sum = 0

        for i, num in enumerate(nums):
            cumulative_sum += num
            remainder = cumulative_sum % k
            if remainder in remainder_map:
                if i - remainder_map[remainder] > 1:
                    return True
                else: 
                    remainder_map[remainder] = i
        return False

sol = Solution()

print(sol.checkSubarraySum(nums = [23,2,4,6,7], k = 6)) # true

print(sol.checkSubarraySum(nums = [23,2,6,4,7], k = 6)) # true

print(sol.checkSubarraySum(nums = [23,2,6,4,7], k = 13)) # false