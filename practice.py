#875 Koko Eating Bananas



from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # need pointers for left and right
        # binary search between 1, max of array?
        l, r = 1, max(piles)
        res = r # worst case scenario, the result will be the max of all piles
        
        # while left less than or equal to right
        while l <= r:
            # get middle
            k = (l + r) // 2 # floor division

            totalTime = 0 # sum when eating at k speed
            for p in piles: # for each pile
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h: # if takes less than or equal to limit
                res = k
                r = k - 1 # move to left to find even lower speed
            else:
                # move to right because you need more time
                l = k + 1
        return res



sol = Solution()

print(sol.minEatingSpeed(piles = [3,6,7,11], h = 8)) # 4

print(sol.minEatingSpeed(piles = [30,11,23,4,20], h = 5)) # 30

print(sol.minEatingSpeed(piles = [30,11,23,4,20], h = 6)) # 23

