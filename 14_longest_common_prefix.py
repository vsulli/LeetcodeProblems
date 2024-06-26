'''
Longest Common Prefix
Leetcode # 14
vsulli
16 June 2024

Write a function to find the longest common prefix
string amongst an array of strings

if there is no common prefix, return an empty string
'''
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        for i in range(len(max(strs))):
            # check slicing from beginning of word to i
            p =([word[:i+1] for word in strs])
            if len(set(p)) != 1:
                return prefix
            prefix = p[0]
        return prefix

sol = Solution()


print(sol.longestCommonPrefix(strs = ["flower","flow","flight"])) # fl

print(sol.longestCommonPrefix(strs = ["dog","racecar","car"])) # ""

print(sol.longestCommonPrefix(strs = ["a"])) # "a"