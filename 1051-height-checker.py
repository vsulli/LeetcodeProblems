'''
Height Checker
Leetcode # 1051
vsulli
10 June 2024

A school is trying to take an annual photo
of all the students. The students are asked to stand
in a single file line in non-decreasing order by height. 
Let this ordering be represented by the integer array expected
expected[i] is the expected height of the ith student in line

You are given an integer array heights representing the current order
the students are standing in. 

return the number of indices where heights[i] != expected[i]
'''

class Solution:
    def heightChecker(self, heights: list[int])->int:
        expected_heights = sorted(heights)
        count = 0

        for i in range(len(heights)):
            if expected_heights[i] != heights[i]:
                count += 1
        return count

sol = Solution()

print(sol.heightChecker(heights = [1, 1, 4, 2, 1, 3])) # 3

print(sol.heightChecker(heights=[5,1,2,3,4])) # 5

print(sol.heightChecker([1,2,3,4,5])) # 0

