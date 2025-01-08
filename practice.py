#2559 
from typing import List
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {"a", "e", "i", "o", "u"}
        count = 0
        prefix_sum = [0] * len(words)
        ans = [0] * len(queries)

        for i in range(len(words)):
            if words[i][0] and words[i][-1] in vowels:
                count += 1
            prefix_sum[i] =  count

        for i in range(len(queries)):
            ans[i] = prefix_sum[queries[i][1]] - (0 if queries[i][0] == 0 else queries[i][0] - 1)
        return ans
          

sol = Solution()

print(sol.vowelStrings(words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]))

print(sol.vowelStrings(words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]))