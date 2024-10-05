#875 Koko Eating Bananas



from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left <= right:
            mid = left + (right - left) // 2
            t = 0
            for pile in piles:
                t += math.ceil(pile / mid)
            
            if t <= h:
                right = mid - 1
            else:
                left = mid + 1
        
        return left



sol = Solution()

print(sol.minEatingSpeed(piles = [3,6,7,11], h = 8)) # 4

print(sol.minEatingSpeed(piles = [30,11,23,4,20], h = 5)) # 30

print(sol.minEatingSpeed(piles = [30,11,23,4,20], h = 6)) # 23

