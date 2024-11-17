'''
My Calendar I
Leetcode # 1497
vsulli
1 October 2024

Given an array of integers arr of even length 
n and an integer k.

We want to divide the array into exactly n / 2 
pairs such that the sum of each pair is divisible by k.

Return true If you can find a way to do that or 
false otherwise.
'''

from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # match up the remainders to the count of numbers with that remainder
        freq = [0] * k
        
        for num in arr:
            remainder = (num % k + k) % k
            freq[remainder] += 1
        
        if freq[0] % 2 != 0:  
            return False
        
        for i in range(1, k // 2 + 1):
            if freq[i] != freq[k - i]:  
                return False
        
        return True

sol = Solution()

print(sol.canArrange(arr = [1,2,3,4,5,10,6,7,8,9], k = 5)) # True

print(sol.canArrange(arr = [1,2,3,4,5,6], k = 7)) # True

print(sol.canArrange(arr = [1,2,3,4,5,6], k = 10)) # False