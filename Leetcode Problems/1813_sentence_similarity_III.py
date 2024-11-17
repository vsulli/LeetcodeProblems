'''
Sentence Similarity III
Leetcode # 1813
vsulli
6 October 2024


'''

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # match from the beginning and end
        # if middle part is the only part that is different then you can return True


        # split each sentence into words
        sentence1 = sentence1.split()
        sentence2 = sentence2.split()

        # makes sure first sentence is longer
        if len(sentence2) > len(sentence1):
            sentence1, sentence2 = sentence2, sentence1

        start, end = 0, 0
        n1, n2 = len(sentence1), len(sentence2)

        # compare from start
        while start < n2 and sentence1[start] == sentence2[start]:
            start += 1
        
        # compare from the end
        while end < n2 and sentence1[n1 - end - 1] == sentence2[n2 - end - 1]:
            end += 1
        
        # check if remainder is in the middle
        return start + end >= n2
    
sol = Solution()

print(sol.areSentencesSimilar(sentence1 = "My name is Haley", sentence2 = "My Haley")) # true


print(sol.areSentencesSimilar(sentence1 = "of", sentence2 = "A lot of words")) # false

print(sol.areSentencesSimilar(sentence1 = "Eating right now", sentence2 = "Eating")) # true


