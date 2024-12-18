''' 
Final Prices with a Special Discount in a Shop
Leetcode # 1475
vsulli
18 December 2024

You are given an integer array prices where prices[i] 
is the price of the ith item in a shop.

There is a special discount for items in the shop. 
If you buy the ith item, then you will receive a 
discount equivalent to prices[j] where j is the 
minimum index such that j > i and prices[j] <= prices[i]. 
Otherwise, you will not receive any discount at all.

Return an integer array answer where answer[i] is the 
final price you will pay for the ith item of the shop, 
considering the special discount.

 
'''
from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # have to look ahead from current index 
        # if that current index is less than or equal to one you're looking at, then use it as discount?
        # if immediate one to right is not smaller, keep searching right
        # restart at index to right of one you're looking at
        # two pointers until one less than end (end will never have discount)
        res = []
        p1 = 0
        p2 = 1
        while p1 < len(prices):
            # advance p2 to next smallest or endd
            while p2 < len(prices) and prices[p2] > prices[p1]:
                p2 += 1
            if p2 < len(prices):
                res.append(prices[p1] - prices[p2])
            elif p2 >= len(prices):
                res.append(prices[p1])
            p1 += 1
            p2 = p1 + 1
        return res

sol = Solution()

print(sol.finalPrices(prices = [8,4,6,2,3])) # Output: [4,2,4,2,3]

print(sol.finalPrices(prices = [1,2,3,4,5])) # [1,2,3,4,5]

print(sol.finalPrices(prices = [10,1,1,6])) # [9,0,1,6]