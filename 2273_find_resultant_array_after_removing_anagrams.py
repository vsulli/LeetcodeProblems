'''
Find Resultant Array After Removing Anagrams
Leetcode # 2273
vsulli
17 July 2024

You are given a 0-indexed string array words, 
where words[i] consists of lowercase English 
letters.

In one operation, select any index i such 
that 0 < i < words.length and words[i - 1] 
and words[i] are anagrams, and delete words[i] 
from words. Keep performing this operation as 
long as you can select an index that satisfies 
the conditions.

Return words after performing all operations. 
It can be shown that selecting the indices for 
each operation in any arbitrary order will lead 
to the same result.

An Anagram is a word or phrase formed by 
rearranging the letters of a different word 
or phrase using all the original letters 
exactly once. For example, "dacb" is an 
anagram of "abdc".
'''
class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        # initialize first pointer left
        # check right pointer against all ones to right until you reach a different pattern
        # change value of left pointer to this index
        # change value of right pointer to this index + 1
            # increment this right pointer
        # not best runtime
        i1 = 0
        i2 = 1

        while i2 <= len(words) - 1 and i1 != i2:

            while i2 <= len(words) - 1 and sorted(words[i1]) == sorted(words[i2]):
                del words[i2]
            i1 = i2
            i2 = i1 + 1
            
        return words

sol = Solution()

print(sol.removeAnagrams(words = ["abba","baba","bbaa","cd","cd"])) # ["abba","cd"]

print(sol.removeAnagrams(words = ["a","b","c","d","e"])) # ["a","b","c","d","e"]

