# 242 Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letter_counts = [0] * 26 # needs to be length of alphabet to fit for each character

        for i in range(len(s)):
            letter_counts[ord(s[i]) - ord('a')] += 1
            letter_counts[ord(t[i]) - ord('a')] -= 1
        
        for c in letter_counts:
            if c != 0:
                return False

        return True

sol = Solution()

print(sol.isAnagram(s = "anagram", t = "nagaram"))

print(sol.isAnagram(s = "rat", t = "car"))