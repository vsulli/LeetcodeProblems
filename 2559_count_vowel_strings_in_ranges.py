#2559 count vowel strings in ranges

from typing import List
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ans = []
        vowels = {"a", "e", "i", "o", "u"}
        prefix_sum  = [0] * len(words)
        count = 0

        # calculate prefix_sum by looping through entire words array
        for i in range(len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                count += 1
                prefix_sum[i] = count 
            else:
                prefix_sum[i] = count
        
        for i in range(len(queries)):
            c_query = queries[i]
            res = prefix_sum[c_query[1]] - (0 if c_query[0] == 0 else prefix_sum[c_query[0] - 1])
            ans.append(res)
        
        return ans
sol = Solution()

print(sol.vowelStrings(words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]))
#[2, 3, 0]
print(sol.vowelStrings(words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]))
# [3, 2, 1]