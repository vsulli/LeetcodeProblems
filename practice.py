# leetcode # 271 Encode and Decode Strings

from typing import List

class Solution:

    def encode(self, strs: List[str])-> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res

        

sol = Solution()

encoded = sol.encode(["we","say",":","yes"])
print(encoded)
print(sol.decode(encoded))

encoded = sol.encode(["neet","code","love","you"])
print(sol.decode(encoded))
