#49 group anagrams

from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []

        # sort letters of each word, if they match dict key,
        #  then store under same key
        anagram_dict = {} # sorted_letter: [word]

        for word in strs:
            if tuple(sorted(word)) in anagram_dict.keys():
                anagram_dict[tuple(sorted(word))].append(word)
            else:
                anagram_dict[tuple(sorted(word))] = [word]
        
        for value in anagram_dict.values():
            ans.append(value)

        return ans

sol = Solution()

print(sol.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))

print(sol.groupAnagrams(strs = [""]))

print(sol.groupAnagrams(strs = ["a"]))