# 242 - Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

sol = Solution()

print(sol.isAnagram(s = "anagram", t = "nagaram"))

print(sol.isAnagram(s = "rat", t = "car"))