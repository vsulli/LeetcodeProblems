# 20 valid parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        opcl = dict(('()', '[]', '{}'))
        # Create stack data structure...
        stack = []
        # Traverse each charater in input string...
        for idx in s:
            # If open parentheses are present, append it to stack...
            if idx in '([{':
                stack.append(idx)
            # If the character is closing parentheses, check that the same type opening parentheses is being pushed to the stack or not...
            # If not, we need to return false...
            elif len(stack) == 0 or idx != opcl[stack.pop()]:
                return False
        # At last, we check if the stack is empty or not...
        # If the stack is empty it means every opened parenthesis is being closed and we can return true, otherwise we return false...
        return len(stack) == 0
    
sol = Solution()


print(sol.isValid(s = "()")) # check right # true

print(sol.isValid(s = "()[]{}")) # true

print(sol.isValid(s = "(]")) # false

print(sol.isValid(s = "([])")) # true



print(sol.isValid("([])")) # true