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
        # need a way to match parentheses
        # how to know when at innermost parenthesis?
        # stack - store indices of left parenthesis
        # loop until get to first closing parenthesis
        # can reverse string in place
        parentheses = []
        for i in range(len(s)):
            if s[i] == "(":
                parentheses.append(i)
            if s[i] == ")":
                left = parentheses.pop()
                # need to reverse between ( + 1 and current i-1
                s[left+1:i] = s[left+1:i:-1]
                # delete indices of the parentheses
                del s[left]
                del s[i]
        return s


sol = Solution()

print(sol.reverseParentheses(s = "(abcd)")) # "dcba"

print(sol.reverseParentheses(s = "(u(love)i)")) # "iloveu"

print(sol.reverseParentheses(s = "(ed(et(oc))el)")) # "leetcode"
# co
# octe
# ed octe el -> leetcode
