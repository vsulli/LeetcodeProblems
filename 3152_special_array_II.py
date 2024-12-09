'''
Special Array II
Leetcode # 3152
vsulli
9 December 2024

An array is considered special if every
 pair of its adjacent elements contains 
 two numbers with different parity.

You are given an array of integer nums 
and a 2D integer matrix queries, where 
for queries[i] = [fromi, toi] your 
task is to check that 
subarray
 nums[fromi..toi] is special or not.

Return an array of booleans answer 
such that answer[i] is true if 
nums[fromi..toi] is special.


parity means even or odd?
'''

# prefix sum
from typing import List
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        prefix = [0] * n  # Prefix array to count special pairs

        # Build the prefix array
        for i in range(1, n):
            prefix[i] = prefix[i - 1]
            if (nums[i - 1] % 2 == 0 and nums[i] % 2 == 0) or (nums[i - 1] % 2 != 0 and nums[i] % 2 != 0):
                prefix[i] += 1

        result = []  # Result list

        # Process each query
        for left, right in queries:
            special_count = prefix[right] -prefix[left]
            result.append(special_count == 0)

        return result
    

sol = Solution()

print(sol.isArraySpecial(nums = [3,4,1,2,6], queries = [[0,4]]))

print(sol.isArraySpecial(nums = [4,3,1,6], queries = [[0,2],[2,3]]))