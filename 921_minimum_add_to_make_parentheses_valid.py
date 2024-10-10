'''
Minimum Add to Make Parentheses Valid
Leetcode # 921
vsulli
9 October 2024

A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), 
where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, 
you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening 
parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.

'''

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # stack?
        # need to return remainder of string or remainder of stack?
        count = 0
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append("(")
            elif stack and stack[-1] == "(" and s[i] == ")":
                stack.pop()
                count += 2
            else:
                stack.append(s[i])

        # return greater of stack or string?
        return len(stack) if stack else (len(s) - count)


sol = Solution()

print(sol.minAddToMakeValid(s = "())")) # 1

print(sol.minAddToMakeValid(s = "(((")) # 3

print(sol.minAddToMakeValid(s = "()))((")) # 4