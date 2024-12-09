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


parity means 
'''
from typing import List
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        answers = [] 
        # loop through queries with two pointers?
        # if one is even and other is odd then return false for that query
        for query in queries:
            p =query[0]
            for i in range(query[0]+1, query[1]):
                # if p and i nums are both even or both odd return False
                if (nums[p] % 2 == 0 and nums[i] % 2 == 0) or (nums[p] % 2 != 0 and nums[i] % 2 != 0):
                    answers.append(False)
                    continue # go to next iteration
                p += 1
            answers.append(True)
        return answers
sol = Solution()

print(sol.isArraySpecial(nums = [3,4,1,2,6], queries = [[0,4]]))

print(sol.isArraySpecial(nums = [4,3,1,6], queries = [[0,2],[2,3]]))