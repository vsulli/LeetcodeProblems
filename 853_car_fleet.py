'''
Car Fleet
Leetcode # 853
vsulli
11 July 2024

There are n cars at given miles 
away from the starting mile 0, 
traveling to reach the mile target.

You are given two integer array 
position and speed, both of length n, 
where position[i] is the starting 
mile of the ith car and speed[i] is 
the speed of the ith car in miles per 
hour.

A car cannot pass another car, but it 
can catch up and then travel next to it 
at the speed of the slower car.

A car fleet is a car or cars driving 
next to each other. The speed of the car 
fleet is the minimum speed of any car 
in the fleet.

If a car catches up to a car fleet at 
the mile target, it will still be 
considered as part of the car fleet.

Return the number of car fleets that 
will arrive at the destination.
 
'''

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # create an array of pairs
        # iterate through array from right to left 
        # if cars are going to collide, left car will have lower time than
        # right car to reach target

        stack = []
        pair = [[p, s] for p, s in zip(position, speed)]
        # reverse sorted order
        for p, s in sorted(pair)[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)



sol = Solution()

print(sol.carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]))
# 3
'''
print(sol.carFleet(target = 10, position = [3], speed = [3])) # 1
'''