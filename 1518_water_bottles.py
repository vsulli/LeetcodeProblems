'''
Water Bottles
Leetcode # 1518
vsulli
7 July 2024

There are numBottles water bottles 
that are initially full of water. 
You can exchange numExchange empty 
water bottles from the market with 
one full water bottle.

The operation of drinking a full 
water bottle turns it into an 
empty bottle.

Given the two integers numBottles 
and numExchange, return the maximum 
number of water bottles you can drink.
'''

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        max_drinks = 0
        empty = 0

        while True:
            max_drinks += numBottles
            empty += numBottles
            numBottles = 0

            numBottles = empty // numExchange
            empty = empty % numExchange

            if numBottles == 0:
                break
        return max_drinks 

sol = Solution()

print(sol.numWaterBottles(numBottles = 9, numExchange = 3)) # 13

print(sol.numWaterBottles(numBottles = 15, numExchange = 4)) # 19