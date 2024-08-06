''' 
Minimum Number of Pushes to Type Word II
Leetcode # 3016
vsulli
6 August 2024

You are given a string word containing 
lowercase English letters.

Telephone keypads have keys mapped with 
distinct collections of lowercase English 
letters, which can be used to form words by 
pushing them. For example, the key 2 is 
mapped with ["a","b","c"], we need to push 
the key one time to type "a", two times to 
type "b", and three times to type "c" .

It is allowed to remap the keys numbered 2
 to 9 to distinct collections of letters. 
 The keys can be remapped to any amount of 
 letters, but each letter must be mapped 
 to exactly one key. You need to find the 
 minimum number of times the keys will be 
 pushed to type the string word.

Return the minimum number of pushes needed 
to type word after remapping the keys.

An example mapping of letters to keys on a 
telephone keypad is given below. Note
 that 1, *, #, and 0 do not map to any letters.
'''
from collections import Counter, OrderedDict

class Solution:
    def minimumPushes(self, word: str) -> int:
        pushes = 0
        # Counter creates a dictionary with letters as keys and frequency as values
        freq_dict = Counter(word)
        freq_dict = freq_dict.most_common()
        

        # get frequency for each character at put in dict
        # sort by frequency in descending order
        # keep a count of distinct as you loop through each key
        #   after count reaches 8, increase cost to 2, 3, etc.
        distinct_chars = 0
        cost = 1
        # get values from freq dict in descending order
        for v in freq_dict:
            pushes += v[1] * cost
            distinct_chars += 1
            if distinct_chars % 8 == 0:
                cost += 1

        return pushes

sol = Solution()

print(sol.minimumPushes(word = "abcde")) # 5
# distinct chars: abcde - 5 - less than 8, so all one push 1x5 = 5
# a = 1 push on key 2
# b = 1 push on key 3...
print(sol.minimumPushes(word = "xyzxyzxyzxyz")) # 12
# distinct chars: xyz = 3 - less than 8, so all one push 1x12 = 12

print(sol.minimumPushes(word = "aabbccddeeffgghhiiiiii")) # 24
# distinct chars: 9 - will want to assign most frequently used chars to first 8 slots

