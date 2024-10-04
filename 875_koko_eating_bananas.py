'''
Koko Eating Bananas
Leetcode # 875
vsulli
4 October 2024

Koko loves to eat bananas. There are n piles of bananas, 
the ith pile has piles[i] bananas. The guards have 
gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of 
k. Each hour, she chooses some pile of bananas and eats 
k bananas from that pile. If the pile has less than k 
bananas, she eats all of them instead and will not eat 
any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating 
all the bananas before the guards return.

Return the minimum integer k such that she can eat all 
the bananas within h hours.
'''
from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        if h == len(piles):
            return max(piles)
        
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res

   

sol = Solution()

print(sol.minEatingSpeed(piles = [3,6,7,11], h = 8)) # 4

print(sol.minEatingSpeed(piles = [30,11,23,4,20], h = 5)) # 30

print(sol.minEatingSpeed(piles = [30,11,23,4,20], h = 6)) # 23
