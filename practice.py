#49 group anagrams

from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        res = []

        for s in strs:
            if tuple(sorted(s)) in groups:
                groups[tuple(sorted(s))].append(s)
            else:
                groups[tuple(sorted(s))] = [s]
        
        for k in groups:
            res.append(groups.get(k))
        return res

sol = Solution()

print(sol.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))

print(sol.groupAnagrams(strs = [""]))

print(sol.groupAnagrams(strs = ["a"]))