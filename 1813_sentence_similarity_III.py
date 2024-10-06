'''
Sentence Similarity III
Leetcode # 1813
vsulli
6 October 2024


'''

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
    # as long as indices of different words is all in a row, then possible to insert?
    # take longer sentence as guide
    # for each index in this sentence, check if it exists in other sentence and get the indices
        isSimilar = True

        
        # convert each string to a list, splitting by space
        sentence2 = sentence2.split()
        for w in sentence2:
            print(w)

        return isSimilar

sol = Solution()

print(sol.areSentencesSimilar(sentence1 = "My name is Haley", sentence2 = "My Haley")) # true

print(sol.areSentencesSimilar(sentence1 = "of", sentence2 = "A lot of words")) # false
# would have to insert before and after

print(sol.areSentencesSimilar(sentence1 = "Eating right now", sentence2 = "Eating"))