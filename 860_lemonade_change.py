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


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        #customers come to you in the order given - queue
        # provide correct change so that the net transaction the customer pays $5
        # don't have change in hand at first
        # return true if you can provide every customer with correct change, false otherwise
        correct_change = True
        change = 0

        for bill in bills:
            print("bill " + str(bill))
            print("change: " + str(change))
            change_due = bill - 5
            print("change due: " + str(change_due))
            print("--------")
            if change_due <= 0:
                change += bill
                
            elif change - change_due < 0:
                return False
            
            elif change_due > 0:
                change -= (bill - 5)

            

        return correct_change

sol = Solution()

print(sol.lemonadeChange(bills = [5,5,5,10,20])) # true

'''

print(sol.lemonadeChange(bills = [5,5,10,10,20])) # false
'''