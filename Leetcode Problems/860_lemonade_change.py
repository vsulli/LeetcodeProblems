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
        # multiple ways to give change for 20s
        #prioritize giving larger bills as change
        # greedy solution
        # O(n) time O(1) space

        five = 0
        ten = 0

        for b in bills:
            if b == 5:
                five += 1
            if b == 10:
                ten += 1

            change = b - 5
            if change == 5:
                if five > 0:
                    five -= 1
                else:
                    return False
                
            elif change == 15:

                # 5 and 10
                if five > 0 and ten > 0:
                    five, ten = five - 1, ten - 1

                # 3 5's
                elif five >= 3:
                    five -= 3
                else: 
                    return False
        return True



sol = Solution()

print(sol.lemonadeChange(bills = [5,5,5,10,20])) # true



print(sol.lemonadeChange(bills = [5,5,10,10,20])) # false
