'''
Valid Parentheses
Leetcode # 20
vsulli
16 June 2024

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        valid = True
        symbols = {')': '(', '}': '{', ']': '['} # hashmap of corr symbol
        # loop through adding to stack?
        # when you reach right symbol, 
        # pop from stack and match to symbol value
            # if they don't match then return False
        l_stack = []
        for c in s:
            if c not in symbols:
                l_stack.append(c)
            else:
                if not l_stack:
                    return False
                l_symbol = l_stack.pop()
                if l_symbol != symbols.get(c):
                    return False
        if l_stack:
            return False
        return valid