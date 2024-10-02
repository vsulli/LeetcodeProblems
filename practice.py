#1497. Check If Array Pairs Are Divisible by k


from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # need to loop through array finding what the remainder is for each number
        # store that in a dictionary rem: count
        # make sure that for each key, equal count
        # how to handle negative numbers?
        divisible = True

        freq_rem = {}

        for i in range(len(arr)):
            rem = arr[i] % 5
            if rem in freq_rem:
                freq_rem[rem] += 1
            else:
                freq_rem[rem] = 1

        # print(freq_rem)
        
        for key in freq_rem:
            if not(freq_rem.get(key) % 2 == 0):
                return False
        return divisible

sol = Solution()

print(sol.canArrange(arr = [1,2,3,4,5,10,6,7,8,9], k = 5)) # true

print(sol.canArrange(arr = [1,2,3,4,5,6], k = 7)) # true

print(sol.canArrange(arr = [1,2,3,4,5,6], k = 10)) # false

