# lc # 271 encode and decode strings

from typing import List
class Solution:

    def encode(self, strs: List[str])-> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res 

    def decode(self, strs: str)->List[str]:
        res = []
        i = 0

        while i < len(strs):
            j = i
            while strs[j] != "#":
                j += 1
            length = int(strs[i:j])
            i = j + 1
            j = i + length
            res.append(strs[i:j])
            i = j
        return res 

sol = Solution()

encoded = sol.encode(["neet","code","love","you"]) # #4neet#4code#4love#3you

print(sol.decode(encoded))