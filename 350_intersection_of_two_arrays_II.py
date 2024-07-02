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
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        # answer will contain numbers in both, 
        # if appears multiple times in both arrays then answer will have that too
        # result can be in any order
        # sort nums first
        # keep count of current number
        # if in one, but not other, skip
        # only matters length of shortest array
        ans = []
        for n in min(nums1, nums2, key = len):
            if n in nums1 and n in nums2:
                ans.append(n)


        

        return ans

sol = Solution()


print(sol.intersect(nums1 = [1,2,2,1], nums2 = [2,2])) # [2,2]

print(sol.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4])) # [4,9]

print(sol.intersect(nums1 = [4,4,4], nums2 = [9,4,9,8,4])) # [4,9]
