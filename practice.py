# 271 Encode and Decode Strings
# Neetcode

from typing import List

class Solution:
    def encode(self, strs: List[str])-> str:
        res = ''
        # separate each word on the ">" character
        for w in strs:
            res += w + ">"
        return res

    def decode(self, s: str)-> List[str]:
        res = []
        w = ""
        # increment pointer through word, when you reach special symbol, append word to res
        p = 0
        while p != (len(s)):
            if s[p] == ">":
                res.append(w)
                w = ""
            else:
                w += s[p]
            p += 1
        return res

sol = Solution()

encoded = sol.encode(["neet","code","love","you"])
print(encoded)
print(sol.decode(encoded))

encoded2 = sol.encode(["we","say",":","yes"])
print(encoded2)
print(sol.decode(encoded2))