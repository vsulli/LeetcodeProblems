# lc # 271 encode and decode strings

from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for w in strs:
            res += "#" + str(len(w))+w
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        p = 0
        while p!= len(s):
            # if index is symbol, take next index and copy that range to result
            # set pointer to index after end
            if s[p] == '#':
                res.append(s[p+2:int(s[p+1])+p+2]) #6   n7  e11  
                p = int(s[p+1])+p+2
        return res

sol = Solution()

encoded = sol.encode(["neet","code","love","you"]) # #4neet#4code#4love#3you

print(sol.decode(encoded))