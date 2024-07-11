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

class Solution:
    def reverseParentheses(self, s: str) -> str:
        pass

sol = Solution()

print(sol.reverseParentheses(s = "(abcd)")) # "dcba"

print(sol.reverseParentheses(s = "(u(love)i)")) # "iloveu"

print(sol.reverseParentheses(s = "(ed(et(oc))el)")) # "leetcode"