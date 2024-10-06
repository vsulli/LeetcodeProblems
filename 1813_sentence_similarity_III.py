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
        match_indices = [] # add the indices of where the word occurs in first sentence and second sentence

        sentence1 = sentence1.split()
        sentence2 = sentence2.split()

        # use two pointers?
        # start with longer sentence
        # keep track of indices of gap?
        # if you reach another gap when you already have a gap, then return false
        # if you reach end of longer sentence with no matches at all, return false?

        p1, p2 = 0, 0
        gap = False

        # first sentence longer
        if len(sentence1) > len(sentence2):
            while p1 <= len(sentence1) - 1:
                if  p2 <= len(sentence2) - 1 and sentence1[p1] == sentence2[p2]:
                    p1 += 1
                    p2 += 1
                elif gap == True:
                    return False
                else:
                    gap = True
                    while p1 <= len(sentence1) - 1 and p2 <= len(sentence2) - 1 and sentence1[p1] != sentence2[p2]:
                        p1 += 1

        '''
        # second sentence longer
        else:
        '''
        return isSimilar

sol = Solution()

print(sol.areSentencesSimilar(sentence1 = "My name is Haley", sentence2 = "My Haley")) # true
# "My" occurs at index 0 for both
# "Haley" occurs at index 3 for 1st, 1 for second
# [[0, 0], [3, 1]]

'''
print(sol.areSentencesSimilar(sentence1 = "of", sentence2 = "A lot of words")) # false
# would have to insert before and after
# "of" occurs at position 0 for 1st, 2 for second
# since not the first position for 2nd sentence, know that there are matches before and after
# [[0, 2]]
'''
print(sol.areSentencesSimilar(sentence1 = "Eating right now", sentence2 = "Eating")) # true
# only one match and both in same position, can insert rest either before or after, return true
# [[0, 0]]

