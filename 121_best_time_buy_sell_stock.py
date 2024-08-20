'''
Best Time to Buy and Sell Stock
Leetcode # 121
vsulli
20 August 2024

You are given an array prices where 
prices[i] is the price of a given stock on the ith day.

You want to maximize your profit 
by choosing a single day to buy 
one stock and choosing a different 
day in the future to sell that stock.

Return the maximum profit you can 
achieve from this transaction. 
If you cannot achieve any profit, return 0.
'''

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # want max price 
        # need two pointers
        max_profit = 0
        bp = 0
        sp = 1
        while sp < len(prices):
            if prices[bp] < prices[sp]:
                profit = prices[sp] - prices[bp]
                max_profit = max(max_profit, profit)
            else:
                bp = sp
            sp += 1

        return max_profit

sol = Solution()
print(sol.maxProfit(prices = [7,1,5,3,6,4])) # output: 5

print(sol.maxProfit(prices = [7,6,4,3,1])) # output: 0

print(sol.maxProfit(prices = [1, 2])) # output: 1