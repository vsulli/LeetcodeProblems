'''
Generate Parentheses
Leetcode # 22
vsulli
6 July 2024

Given n pairs of parentheses, write a function 
to generate all combinations of 
well-formed parentheses.

'''

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # backtracking solution
        # only add open if open < n
        # only add closing parenthesis if closed < open
        # return solution open == closed == n

        # recursive
        stack = []
        res = []
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return 
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        backtrack(0, 0)
        return res


sol = Solution()

print(sol.generateParenthesis(n = 3))

print(sol.generateParenthesis(n = 2))

print(sol.generateParenthesis(n = 1))

