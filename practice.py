# 2559

from typing import List
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ans = [0] * len(queries)
        vowels = {"a", "e", "i", "o", "u"}
        prefix_sums = [0] * len(words)
        count = 0

        for i in range(len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                count += 1
                prefix_sums[i] = count 
            else:
                prefix_sums[i] = count
        
        # now have to loop through queries
        for i in range(len(queries)):
            query = queries[i]
            


sol = Solution()

print(sol.vowelStrings(words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]))

print(sol.vowelStrings(words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]))