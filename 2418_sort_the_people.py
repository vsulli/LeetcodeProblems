''' 
Sort the People
Leetcode # 2418
vsulli
22 July 2024


'''

class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        res = list(zip(heights, names))
        res.sort(key=lambda x: x[0], reverse=True)
        # can unzip using zip and * operator
        res = list(zip(*res))
        return res[1]



sol = Solution()

print(sol.sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170]))
# ["Mary","Emma","John"]

print(sol.sortPeople(names = ["Alice","Bob","Bob"], heights = [155,185,150]))
# ["Bob","Alice","Bob"]