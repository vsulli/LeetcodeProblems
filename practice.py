# leetcode # 271 Encode and Decode Strings
p = 0
s = '#3say#1:#3yes'
print(s[p+2:p+int(s[p+1])+2])

'''
from typing import List

class Solution:

    def encode(self, strs: List[str])-> str:
        res = ''
        # append '#' + length of word + word
        for w in strs:
            res += '#' + str(len(w)) + w
        return res


    def decode(self, s: str)-> List[str]:
        res = []
        p = 0
        # copy from # , num units to right
        while p != len(s):
            if s[p] == '#':
                res.append(s[p+2:p+s[p+1]+2])

        

sol = Solution()

print(sol.encode(["we","say",":","yes"]))

print(sol.encode(["neet","code","love","you"]))
'''