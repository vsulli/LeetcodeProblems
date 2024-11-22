# 49 group anagrams

from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str])->List[List[str]]:
        res = []
        word_dict = {} # sorted(key) : [words]

        for w in strs:
            if tuple(sorted(w)) in word_dict:
                word_dict[tuple(sorted(w))].append(w)
            else:
                word_dict[tuple(sorted(w))] = [w]

        for v in word_dict.values():
            res.append(v)
        return res
        
sol = Solution()

print(sol.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
print(sol.groupAnagrams(strs = [""]))