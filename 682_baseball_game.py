'''
Baseball Game
Leetcode # 682
vsulli
30 June 2024

You are keeping the scores for a baseball 
game with strange rules. At the beginning of 
the game, you start with an empty record.

You are given a list of strings operations, 
where operations[i] is the ith operation you 
must apply to the record and is one of the 
following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous 
two scores.
'D'.
Record a new score that is the double of the previous 
score.
'C'.
Invalidate the previous score, removing it from the 
record.
Return the sum of all the scores on the record after 
applying all the operations.

The test cases are generated such that the answer and 
all intermediate calculations fit in a 32-bit integer 
and that all operations are valid.
'''

class Solution:
    def calPoints(self, operations: list[str]) -> int:
        score = []
        for i in range(len(operations)):

            # if C then remove previous score
            if operations[i] == "C":
                del score[-1]
            elif operations[i] == "D":
                score.append(score[-1] * 2)
            elif operations[i] == "+":
                score.append(score[-1] + score[-2])
            else:
                score.append(int(operations[i]))

        if not score:
             return 0 
        else:
            return sum(score)

sol = Solution()

print(sol.calPoints(operations = ["5","2","C","D","+"])) # 30

print(sol.calPoints(operations = ["5","-2","4","C","D","9","+","+"])) # 27

print(sol.calPoints(operations = ["1", "C"])) # 0