# topics - array, string, prefix sum
from typing import List
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # perform precomputations on words
        # create prefix sum array prefixSum to store the cumulative counts of vowel strings in words
        # prefixSum[i] would contain the total number of vowel strins from 1st element up to index i
        ans = [0] * len(queries)
        vowels = {"a", "e", "i", "o", "u"}
        prefix_sum = [0] * len(words)
        sum = 0
        for i in range(len(words)):
            current_word = words[i]
            # check beginning and end of word
            if (current_word[0] in vowels and 
            current_word[len(current_word) - 1] in vowels
            ):
                sum += 1
            prefix_sum[i] = sum
        
        for i in range(len(queries)):
            current_query = queries[i]
            ans[i] = prefix_sum[current_query[1]] - (
                0 if current_query[0] == 0 else prefix_sum[current_query[0] - 1]
            )
        
        return ans

sol = Solution()

print(sol.vowelStrings(words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]))

print(sol.vowelStrings(words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]))