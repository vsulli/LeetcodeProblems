#2559 count vowel strings in ranges
# neetcode solution

from typing import List
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel_set = set("aeiou")
        prefix_sum = [0] * (len(words) + 1)
        prev = 0
        for i, w in enumerate(words):
            if w[0] in vowel_set and w[-1] in vowel_set:
                prev += 1

            prefix_sum[i + 1] = prev
        print(prefix_sum)
        res = [0] * len(queries)
        for i, q in enumerate(queries):
            l, r = q
            res[i] = prefix_sum[r + 1] - prefix_sum[l]
        return res

sol = Solution()

print(sol.vowelStrings(words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]))
#[2, 3, 0]
# prefix_sum = [0, 1, 1, 2, 3, 4]
print(sol.vowelStrings(words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]))
# [3, 2, 1]
# prefix_sum = [0, 1, 2, 3]