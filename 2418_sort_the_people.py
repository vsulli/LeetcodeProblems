''' 
Sort the People
Leetcode # 2418
vsulli
22 July 2024


'''

class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        res = [None] * len(heights)
        for i, n in enumerate(names):
            res[i] = [heights[i], n]

        res.sort(key=lambda x: x[0], reverse=True)
        for i in range(len(res)):
            temp = res[i][1]
            res[i] = temp
        return res



sol = Solution()

print(sol.sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170]))
# ["Mary","Emma","John"]

print(sol.sortPeople(names = ["Alice","Bob","Bob"], heights = [155,185,150]))
# ["Bob","Alice","Bob"]