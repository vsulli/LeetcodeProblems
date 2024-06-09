'''
Group Anagrams
Leetcode # 49
vsulli
9 June 2024

Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An anagram is a word or phrase formed by rearranging the 
letters of a different word or phrase, typically using 
all the original letters exactly once.
'''

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = []

        # count letters for each word
        # sort letters of each word, if they match then store under same key
        anagram_dict = {} # sorted_letter: [word]

        for word in strs:
            if sorted(word) in anagram_dict.keys():
                anagram_dict[sorted(word)].append(word)
            else:
                anagram_dict[(sorted(word))] = [word]
        
        for value in anagram_dict.values():
            ans.append(value)
        return ans
    
sol = Solution()

print(sol.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
# [["bat"],["nat","tan"],["ate","eat","tea"]]

print(sol.groupAnagrams(strs = [""]))
# [[""]]

print(sol.groupAnagrams(strs = ["a"]))
# [["a"]]