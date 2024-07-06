'''
Letter Combinations of a Phone Number
Leetcode # 17
vsulli
6 July 2024

Given a string containing digits from 
2-9 inclusive, return all possible 
letter combinations that the number 
could represent. Return the answer in any order.

A mapping of digits to letters (just 
like on the telephone buttons) is given 
below. Note that 1 does not map to any letters.

'''
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        letters = []
        res = []
        combo_len = 0
        for n in digits:
            combo_len += len(digit_letters[n])  
        # 1 isn't included
        digit_letters = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], 
                        "4": ["g", "h", "i"], "5": ["j", "k", "l"], 
                         "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], 
                         "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}

        def backtrack():
            # exit condition would be length of res as long as all combinations?


sol = Solution()

print(sol.letterCombinations(digits = "23"))
# ["ad","ae","af","bd","be","bf","cd","ce","cf"]

print(sol.letterCombinations(digits = ""))
# []

print(sol.letterCombinations( digits = "2"))
# ["a","b","c"]