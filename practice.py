# leetcode # 271 Encode and Decode Strings

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
                res.append(s[p+2:p+int(s[p+1])+2])
                p = p+int(s[p+1])+2
        return res

        

sol = Solution()

encoded = sol.encode(["we","say",":","yes"])
print(encoded)
print(sol.decode(encoded))

encoded = sol.encode(["neet","code","love","you"])
print(sol.decode(encoded))
