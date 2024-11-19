# 242 - Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        d = [0] * 26

        for i in range(len(s)):
            d[ord(s[i]) - ord('a')] += 1
            d[ord(t[i]) - ord('a')] -= 1
        
        for val in d:
            if val != 0:
                return False
        return True

sol = Solution()

print(sol.isAnagram(s = "anagram", t = "nagaram"))

print(sol.isAnagram(s = "rat", t = "car"))
