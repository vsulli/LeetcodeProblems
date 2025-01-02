from typing import List
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ['a', 'e', 'i', 'o', 'u']
        # add all words to dictionary with index as key?
        res = []
        word_dict = {}
        for i in range(len(words)):
            word_dict[i] = words[i]

        for q in queries:
            count = 0
            for i in range(q[0], q[1] + 1):
                # if starts and ends with a vowel or length 1 and vowel
                # add to result
                if len(word_dict[i]) == 1 and word_dict[i] in vowels:
                    count += 1
                elif word_dict[i][0] in vowels and word_dict[i][-1] in vowels:
                    count += 1
            res.append(count)
        return res

sol = Solution()

print(sol.vowelStrings(words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]))

print(sol.vowelStrings(words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]))