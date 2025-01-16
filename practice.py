from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {} # tuple sorted chars : list []
        for w in strs:
            if tuple(sorted(w)) in words:
                words[tuple(sorted(w))].append(w)
            else:
                words[tuple(sorted(w))] = [w]
        res = []
        for v in words.values():
            res.append(v)
        return res

sol = Solution()

print(sol.groupAnagrams(strs = [""]))

print(sol.groupAnagrams(strs = ["a"]))

print(sol.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
# [["bat"],["nat","tan"],["ate","eat","tea"]]