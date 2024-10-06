'''
Sentence Similarity III
Leetcode # 1813
vsulli
6 October 2024


'''

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        pass
    # as long as indices of different words is all in a row, then possible to insert?


sol = Solution()

print(sol.areSentencesSimilar(sentence1 = "My name is Haley", sentence2 = "My Haley")) # true

print(sol.areSentencesSimilar(sentence1 = "of", sentence2 = "A lot of words")) # false
# would have to insert before and after

print(sol.areSentencesSimilar(sentence1 = "Eating right now", sentence2 = "Eating"))