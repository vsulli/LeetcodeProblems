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
        # ways(n) = ways(n-1) + ways(n-2)
        # always the sum of the two previous

        dp = [0]*(n+2)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
       

        


sol = Solution()

print(sol.climbStairs(n = 2)) # 2 ways (1 + 1) or just (2)

print(sol.climbStairs(n = 3)) #3 (1 + 1 + 1), ( 1 + 2), (2 + 1)

# 2 = 2, 3 = 3, 4 = 5, 5 = 8?