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
        res = []
        # 1 isn't included
        digit_letters = {"2": "abc", "3":"def", 
                        "4": "ghi", "5": "jkl", 
                         "6": "mno", "7": "pqrs", 
                         "8": "tuv", "9": "wxyz"}

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in digit_letters[digits[i]]:
                backtrack(i+1, curStr + c)
        
        if digits:
            backtrack(0, "")

        return res


sol = Solution()

print(sol.letterCombinations(digits = "23"))
# ["ad","ae","af","bd","be","bf","cd","ce","cf"]

print(sol.letterCombinations(digits = ""))
# []

print(sol.letterCombinations( digits = "2"))
# ["a","b","c"]