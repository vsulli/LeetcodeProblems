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
        spaces = () # spaces stack
        while t_ptr != len(target) and s_ptr != len(start):
            # target is at a letter
            if target[t_ptr] == "_":
                t_ptr += 1
            # start and target don't match
            if target[t_ptr] != start[s_ptr]:
                while start[s_ptr] == "_":
                    spaces.push(start[s_ptr])
                    s_ptr += 1
                # start is at a letter now
                # if target is L
                if target[t_ptr] == "L":
                    # use stack? pop off as many to get it to match index of target ptr?
                    # if meet an R, return?
                    temp = s_ptr
                    for _ in range(t_ptr - s_ptr):
                        top = spaces.pop()
                        temp -= 1
                        if top == "R":
                            return False
                    start[s_ptr] = "_"
                    start[temp] = "L"
                    s_ptr += 1
            

                # elif target is R
                t_ptr += 1

            
            t_ptr += 1
        

        return obtainString

sol = Solution()

print(sol.canChange(start = "_L__R__R_", target = "L______RR"))