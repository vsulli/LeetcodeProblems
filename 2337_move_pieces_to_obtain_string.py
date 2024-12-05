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

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        obtainString = True
        # loop through from left to right?
        # pointer on 2nd target
        # get all indices of target string?
        t_ptr = 0
        s_ptr = 0
        target_indices = [None] * len(target) # initialize empty target index array
        for i in range(len(target)):
            if target[i] != "_":
                target_indices[i] = target[i]

        print(target_indices)
        while t_ptr != len(target):
            # only care about indices where L or R
            while target[t_ptr] == None:
                t_ptr += 1
            # if letter is L
            if start[s_ptr] != target[t_ptr] and target[t_ptr] == 'L':
                # go right until you meet a letter
                # if R, return False
                # if L, try to move it backwards to left to correct place
            # if letter is R
            elif start[s_ptr] != target[t_ptr] and target[t_ptr] == 'R':  
                pass
        

        return obtainString

sol = Solution()

print(sol.canChange(start = "_L__R__R_", target = "L______RR"))