# 20 valid parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        symbols = {')': '(', '}':'{', ']':'['}
        
        my_stack = set()
        for symbol in s:
            # if symbol is right, check if left equivalent is in stack
            if symbol in symbols:
                popped = my_stack.pop()
                # check if left is what you get when you look up in stack
                if popped != symbols.get(symbol):
                    return False
            else:
                my_stack.add(symbol)
    
        return len(my_stack) == 0
    
sol = Solution()

'''
print(sol.isValid(s = "()")) # check right # true

print(sol.isValid(s = "()[]{}")) # true

print(sol.isValid(s = "(]")) # false

print(sol.isValid(s = "([])")) # true

'''

print(sol.isValid("([])")) # true