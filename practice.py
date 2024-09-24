# string encode and decode

from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + ''.join(s + ";")
        return res

    def decode(self, s: str) -> List[str]:
        pass


sol = Solution()

print(sol.encode(["neet","code","love","you"]))

print(sol.decode(sol.encode(["neet","code","love","you"])))