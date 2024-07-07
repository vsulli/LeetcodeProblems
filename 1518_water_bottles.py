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
        empty_bottles = 0
        max_drinks = numBottles

        # while you can evenly divide or there is a remainder
        while empty_bottles // numExchange > 0:
            empty_bottles += numBottles - ((numBottles // numExchange) * numExchange)
            numBottles = (numBottles // numExchange)
            max_drinks += numBottles
        

        print("Bottles: " + str(numBottles))
        return max_drinks 

sol = Solution()

print(sol.numWaterBottles(numBottles = 9, numExchange = 3)) # 13

print(sol.numWaterBottles(numBottles = 15, numExchange = 4)) # 19