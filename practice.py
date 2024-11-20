# 49 Group Anagrams

from typing import List

class Solution:
    def groupAnagrams(self, strs:list[str])-> List[List[str]]:
        # hashmap sorted_key: [list of original values]
        # need to store the counts for each letter in the word
        # if sorted of that word matches sorted that's already a key in hashmap, add to list?
        res = []
        str_hashmap = {}        
        
        for s in strs:
            if tuple(sorted(s)) in str_hashmap:
                str_hashmap[tuple(sorted(s))].append(s)
            else:
                str_hashmap[tuple(sorted(s))] = [s]
        
        for k in str_hashmap:
            res.append(str_hashmap[k])

        return res


sol = Solution()

print(sol.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

print(sol.groupAnagrams(strs = [""]))
# Output: [[""]]