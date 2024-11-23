# 242 valid anagram

class Solution:
    def isAnagram(self, s: str, t: str)->bool:
        # check if words are same length
        if len(s) != len(t):
            return False 
        # initialize an array of length of alphabet
        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        for val in count:
            if val != 0:
                return False
        return True

sol = Solution()

print(sol.isAnagram(s = "anagram", t = "nagaram"))
print(sol.isAnagram(s = "rat", t = "car"))
