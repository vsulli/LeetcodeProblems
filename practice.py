# 271 encode and decode strings

from typing import List

class Solution:
    def encode(self, strs:List[str])-> str:
        res = ''
        for w in strs:
            res += str(len(w)) + '#' + w
        return res

    def decode(self, strs:str)->List[str]:
        res = []
        i = 0
        while i < len(strs):
            j = i
            while strs[j] != '#':
                j += 1
            length = int(strs[i:j])
            i = j + 1
            j = i + length
            res.append(strs[i:j])
            i = j
        
        return res

sol = Solution()

encoded = sol.encode(["neet","code","love","you"])
print(encoded)
print(sol.decode(encoded))
