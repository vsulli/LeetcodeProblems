'''
Daily Temperatures
Leetcode # 739
vsulli
9 July 2024

Given an array of integers temperatures 
represents the daily temperatures, 
return an array answer such that answer[i] 
is the number of days you have to wait 
after the ith day to get a warmer temperature. 
If there is no future day for which this is 
possible, keep answer[i] == 0 instead.
 
'''

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)
        
        # using a stack, for each number, put the index of the greatest
        # number up to that point?


        temp_diff = []

        # using a stack
        # keep track of how much greater next index is from last index?
        i1 = 0
        i2 = 1
        max = 0
        while i2 < len(temperatures) - 1:
            if temperatures[i2] > temperatures[i1]:
                answer[i1] = i2 - i1
                i2 += 1
            else:
                temp_diff.append(temperatures[i2] - temperatures[i1])
                i1 += 1
        return answer

sol = Solution()


print(sol.dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73]))
# [1,1,4,2,1,1,0,0]

print(sol.dailyTemperatures(temperatures = [30,40,50,60]))
# [1,1,1,0]


print(sol.dailyTemperatures(temperatures = [30,60,90]))
# [1,1,0]
