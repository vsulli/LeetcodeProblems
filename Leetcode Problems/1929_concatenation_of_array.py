'''
Concatenation of Array
Leetcode # 1929
vsulli
10 June 2024

Given an integer array nums of length n, you want
to create an array ans of length 2n where 
ans[i] == nums[i] and ans[i + n] == nums[i] for
0 <= i < n (0-indexed)

specifically, ans is the concatenation of two nums arrays

return the array ans
'''

class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums*2

sol = Solution()
print(sol.getConcatenation(nums = [1,2,1])) # [1,2,1,1,2,1]

print(sol.getConcatenation(nums = [1,3,2,1])) # [1,3,2,1,1,3,2,1]

