'''
Adding Spaces to a String
Leetcode # 2109
vsulli
3 December 2024

You are given a 0-indexed string s
 and a 0-indexed integer array spaces 
 that describes the indices in the original 
 string where spaces will be added. Each 
 space should be inserted before the character 
 at the given index.

For example, given s = "EnjoyYourCoffee" 
and spaces = [5, 9], we place spaces before 
'Y' and 'C', which are at indices 5 and 9 
respectively. Thus, we obtain "Enjoy Your 
Coffee".
Return the modified string after the spaces 
have been added.

'''
from typing import List

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        index, result = 0, []

        for space in spaces:
            result.append(s[index : space])
            index = space
        
        result.append(s[index :])
        return " ".join(result)
            


sol = Solution()
print(sol.addSpaces(s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]))
print(sol.addSpaces(s = "icodeinpython", spaces = [1,5,7,9]))
print(sol.addSpaces(s = "spacing", spaces = [0,1,2,3,4,5,6]))