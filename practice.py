# 49 Group Anagrams

from typing import List

class Solution:
    def groupAnagrams(self, strs:List[str])->List[List[str]]:
        res = []
        d = {}

        for s in strs:
            if tuple(sorted(s)) in d:
                d[tuple(sorted(s))].append(s)
            else:
                d[tuple(sorted(s))] = [s]
        
        for val in d.values():
            res.append(val)


        return res
    

sol = Solution()

print(sol.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

print(sol.groupAnagrams(strs = [""]))
# Output: [[""]]