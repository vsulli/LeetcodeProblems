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
        # j - sell , i - buy
        max_profit = 0
        buy = 0
        for i in range(len(prices)):
        
            for j in range(i+1, len(prices)-1):
                if prices[j] > prices[i]:
                    max_profit = max(prices[j] - prices[i], max_profit)
            
        return max_profit

sol = Solution()
print(sol.maxProfit(prices = [7,1,5,3,6,4])) # output: 5

print(sol.maxProfit(prices = [7,6,4,3,1])) # output: 0