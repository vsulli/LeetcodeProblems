#242 Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        for v in count:
            if v != 0:
                return False
        return True

sol = Solution()

print(sol.isAnagram(s = "anagram", t = "nagaram"))
print(sol.isAnagram(s = "car", t = "tar"))