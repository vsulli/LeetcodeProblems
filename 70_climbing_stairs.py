'''
Climbing Stairs
Leetcode # 70
vsulli
15 July 2024

You are climbing a staircase. 
It takes n steps to reach the top.

Each time you can either climb 
1 or 2 steps. In how many distinct 
ways can you climb to the top?
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        # need a recursive answer becuase once you check one combo 
        # you need to check all others
        


        


sol = Solution()

print(sol.climbStairs(n = 2)) # 2 ways (1 + 1) or just (2)

print(sol.climbStairs(n = 3)) #3 (1 + 1 + 1), ( 1 + 2), (2 + 1)
