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
        # wormhole solution
        n = len(s)

        open_parentheses_indices = []
        pair = [0] * n

        # first pass - pair parentheses
        for i in range(n):
            if s[i] == "(":
                open_parentheses_indices.append(i)
            if s[i] == ")":
                j = open_parentheses_indices.pop()
                pair[i] = j
                pair[j] = i
        
        # second pass - build result string
        result = []
        curr_index = 0
        direction = 1

        while curr_index < n:
            if s[curr_index] == "(" or s[curr_index] == ")":
                curr_index = pair[curr_index]
                direction = -direction
            else:
                result.append(s[curr_index])
            curr_index += direction
        return "".join(result)
                       


sol = Solution()

print(sol.reverseParentheses(s = "(abcd)")) # "dcba"

print(sol.reverseParentheses(s = "(u(love)i)")) # "iloveu"

print(sol.reverseParentheses(s = "(ed(et(oc))el)")) # "leetcode"
# co
# octe
# ed octe el -> leetcode
