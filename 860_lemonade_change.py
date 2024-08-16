'''
Lemonade Change
Leetcode # 860
vsulli
15 August 2024

At a lemonade stand, each lemonade costs $5. 
Customers are standing in a queue to buy 
from you and order one at a time (in the 
order specified by bills). Each customer 
will only buy one lemonade and pay with 
either a $5, $10, or $20 bill. You must 
provide the correct change to each customer 
so that the net transaction is that the 
customer pays $5.

Note that you do not have any change in hand 
at first.

Given an integer array bills where bills[i] 
is the bill the ith customer pays, return true 
if you can provide every customer with the 
correct change, or false otherwise.
'''
from typing import List
import heapq

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        #customers come to you in the order given - queue
        # provide correct change so that the net transaction the customer pays $5
        # don't have change in hand at first
        # return true if you can provide every customer with correct change, false otherwise
        correct_change = True
        money = []

        for bill in bills:
            change_due = bill - 5
            if sum(money) - change_due < 0:
                return False
            else:
                change = 0
                while change < change_due:
                    money = heapq._heapify_max(money)
                    change += heapq.heappop(money)

            print(money)

        return correct_change

sol = Solution()

print(sol.lemonadeChange(bills = [5,5,5,10,20])) # true



print(sol.lemonadeChange(bills = [5,5,10,10,20])) # false
