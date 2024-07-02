'''
Intersection of Two Arrays II
Leetcode # 350
vsulli
1 July 2024

Given two integer arrays nums1 and 
nums2, return an array of their 
intersection. Each element in the 
result must appear as many times 
as it shows in both arrays and you 
may return the result in any order.
'''

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        arr = [0] * 1001
        result = []
        for n in nums1:
            arr[n] +=1

        for n in nums2:
            if arr[n] > 0:
                result.append(n)
                arr[n] -= 1
        return result[: len(result)]

sol = Solution()


print(sol.intersect(nums1 = [1,2,2,1], nums2 = [2,2])) # [2,2]

print(sol.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4])) # [4,9]

print(sol.intersect(nums1 = [4,4,4], nums2 = [9,4,9,8,4])) # [4,4]
