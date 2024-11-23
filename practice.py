# 242 valid anagram

class Solution:
    def isValid(self, s: str, t: str)->bool:
        return sorted(s) == sorted(t)
sol = Solution()

print(sol.isValid(s = "anagram", t = "nagaram"))
print(sol.isValid(s = "rat", t = "car"))

