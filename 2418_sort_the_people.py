''' 
Sort the People
Leetcode # 2418
vsulli
22 July 2024


'''

class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        n: int = len(names)
        mapping: dict[int, str] = {}  # height -> name (heights are distinct)
        for ind in range(n):
            mapping[heights[ind]] = names[ind]

        heights.sort(reverse=True)
        for ind in range(n):
            h: int = heights[ind]
            names[ind] = mapping[h]

        return names



sol = Solution()

print(sol.sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170]))
# ["Mary","Emma","John"]

print(sol.sortPeople(names = ["Alice","Bob","Bob"], heights = [155,185,150]))
# ["Bob","Alice","Bob"]