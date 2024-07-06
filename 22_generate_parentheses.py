'''
Pass the Pillow
Leetcode # 22
vsulli
6 July 2024

Given n pairs of parentheses, write a function 
to generate all combinations of 
well-formed parentheses.

'''

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # left
        # right
        ans = []
        # lined up
        ans.append("()" * n)
        # inside
        string = "("
        for i in range(n -1):
            string += "()"
        string += ")"
        if string not in ans:
            ans.append(string)

        

        return ans
    # need to generate all combinations of well-formed parentheses
    # 5 combinations with 3
    # n will be 8 at most

    # 1 -- ()
    # 2 -- ()(), (())
    # 3 -- ()()(), (()()), ((())), (())(), ()(())
    # 4 -- ()()()(), (()()()), (((()))), ((()))(), ()((())), (())(())

sol = Solution()

print(sol.generateParenthesis(n = 3))

print(sol.generateParenthesis(n = 2))

print(sol.generateParenthesis(n = 1))

