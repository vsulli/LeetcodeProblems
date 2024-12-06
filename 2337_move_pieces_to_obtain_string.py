'''
Move Pieces to Obtain a String
Leetcode # 2337
vsulli
4 December 2024

You are given two strings start 
and target, both of length n. 
Each string consists only of the 
characters 'L', 'R', and '_' where:

The characters 'L' and 'R' represent 
pieces, where a piece 'L' can move to 
the left only if there is a blank space 
directly to its left, and a piece 'R' 
can move to the right only if there is 
a blank space directly to its right.
The character '_' represents a blank 
space that can be occupied by any of the 
'L' or 'R' pieces.
Return true if it is possible to obtain 
the string target by moving the pieces 
of the string start any number of times. 
Otherwise, return false.
'''

# ordering of L and R should be same
# start R should be at same or smaller
# start L should be at greater or same
class Solution:
    def canChange(self, start: str, target: str) -> bool:
       # if they already match return True
        if start == target:
            return True
        

        pending_L = 0   
        waiting_R = 0    

        # zip joins two tuples together
        for curr, goal in zip(start, target): # curr (_, L) goal
            if goal == 'L':
                if waiting_R > 0:
                    return False
                pending_L += 1
            if curr == 'R':
                if pending_L > 0:
                    return False
                waiting_R += 1  
            if goal == 'R':
                if waiting_R == 0:
                    return False
                waiting_R -= 1   
            if curr == 'L':
                if pending_L == 0:
                    return False
                pending_L -= 1  
        return pending_L == 0 and waiting_R == 0 
sol = Solution()

print(sol.canChange(start = "_L__R__R_", target = "L______RR"))