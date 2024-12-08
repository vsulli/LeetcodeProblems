# encode and decode strings



from typing import List
class Solution:

    def encode(self, strs: List[str])-> str:
        encoded = ""
        # add #- length of word - word
        for w in strs:
            encoded += "#" + str(len(w)) + w
        return encoded

    def decode(self, strs: str)->List[str]:
        # loop through until pointer is at symbol
            # copy to result ptr + 2: ptr + 1 + int(string[ptr])
        res = []
        ptr = 0
        while ptr < len(strs):
            if strs[ptr] == "#":
                res.append(strs[ptr+2:ptr+2+int(strs[ptr+1])])
                ptr = ptr+2+int(strs[ptr+1])
        return res



sol = Solution()

print(sol.decode(sol.encode(["we","say",":","yes"])))
# #2we#3say#1:#3yes

print(sol.decode(sol.encode(["neet","code","love","you"])))
