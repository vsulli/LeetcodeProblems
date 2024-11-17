'''
Evaluate Reverse Polish Notation
Leetcode # 150
vsulli
30 June 2024

You are given an array of strings tokens 
that represents an arithmetic expression 
in a Reverse Polish Notation.

Evaluate the expression. Return an integer 
that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

RPN: operators follow operands
'''
import math

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        
        res = [] # stack 
        for c in tokens:
            if c == "+":
               res.append(res.pop() + res.pop())
            elif c == "-":
                a, b = res.pop(), res.pop()
                res.append(b - a)
            elif c == "*":
                res.append(res.pop() * res.pop())
            elif c == "/":
                a, b = res.pop(), res.pop()
                res.append(int(b / a)) # will round toward 0 in python
            else:
                res.append(int(c))
        return res [0] 

        
        

sol = Solution()

print(sol.evalRPN(tokens = ["18"])) # 18

print(sol.evalRPN(tokens = ["2","1","+","3","*"])) # ((2+1)* 3) = 9

print(sol.evalRPN(tokens = ["4","13","5","/","+"])) # (4 + (13 / 5)) = 6

print(sol.evalRPN(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"])) # 22