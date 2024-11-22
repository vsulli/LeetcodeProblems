# 49 - Group Anagrams

from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        d = {}

        for w in strs:
            if tuple(sorted(w)) in d:
                d[tuple(sorted(w))].append(w)
            else:
                d[tuple(sorted(w))] = [w]
        
        for l in d.values():
            res.append(l)
        return res
    
sol = Solution()

print(sol.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))

print(sol.groupAnagrams(strs = [""]))

print(sol.groupAnagrams(strs = ["a"]))