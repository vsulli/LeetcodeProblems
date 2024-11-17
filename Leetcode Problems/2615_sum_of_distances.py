''' 
Sum of Distances
Leetcode # 2615
vsulli
8 August 2024

You are given a 0-indexed integer 
array nums. There exists an array 
arr of length nums.length, where 
arr[i] is the sum of |i - j| over 
all j such that nums[j] == nums[i] 
and j != i. If there is no such j, 
set arr[i] to be 0.

Return the array arr.
 
'''
from collections import defaultdict


class Solution:
    def distance(self, nums: list[int]) -> list[int]:
        d={}
        for i,num in enumerate(nums):
            if num not in d:
                d[num]=[]
            d[num].append(i)
        answ=[0]*len(nums)
        for num,val in d.items():
            suffixSum=sum(val)
            preffixSum=0
            s=len(val)
            p=0
            for i in val:
                preffixSum+=i
                p+=1
                suffixSum-=i
                s-=1
                answ[i]=-preffixSum + p*i - s*i + suffixSum
        return answ     

sol = Solution()

print(sol.distance(nums = [1,3,1,1,2])) # [5, 0, 3, 4, 0]

print(sol.distance(nums = [0,5,3])) # [0, 0, 0]