'''
Reverse Substrings Between Each Pair of Parentheses
Leetcode # 1190
vsulli
10 July 2024

You are given a string s that consists 
of lower case English letters and brackets.

Reverse the strings in each pair of 
matching parentheses, starting from 
the innermost one.

Your result should not contain any 
brackets.
 
'''

from collections import deque


class Solution:
    def reverseParentheses(self, s: str) -> str:
        open_parentheses_indices = deque()
        result = []

        for current_char in s:
            if current_char == "(":
                # store current len as start index
                open_parentheses_indices.append(len(result))
            elif current_char == ")":
                start = open_parentheses_indices.pop()
                # reverse substring between matching parentheses
                result[start:] = result[start:][::-1]
            else:
                # append non-parenthesis characters
                result.append(current_char)
        return "".join(result)
                       


sol = Solution()

print(sol.reverseParentheses(s = "(abcd)")) # "dcba"

print(sol.reverseParentheses(s = "(u(love)i)")) # "iloveu"

print(sol.reverseParentheses(s = "(ed(et(oc))el)")) # "leetcode"
# co
# octe
# ed octe el -> leetcode
