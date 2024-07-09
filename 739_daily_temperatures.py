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
        # answer[i] tells you how many days to wait until you get a warmer temperature
        # will be 0 if there is no warmer day
        # last index will always be 0
        for i in range(len(temperatures)-1):
            for j in range(i+1, len(temperatures)-1):
                if temperatures[j] > temperatures[i]:
                    answer[i] = j - i
                    break

        return answer

sol = Solution()

print(sol.dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73]))
# [1,1,4,2,1,1,0,0]

print(sol.dailyTemperatures(temperatures = [30,40,50,60]))
# [1,1,1,0]

print(sol.dailyTemperatures(temperatures = [30,60,90]))
# [1,1,0]
