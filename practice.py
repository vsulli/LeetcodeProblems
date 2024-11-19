# 242 - Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # count of each character must be the same and they must be the same length
        if len(s) != len(t):
            return False
        
        isAnagram = True
        count_s = {}
        count_t = {}

        for i in range(len(s)):
            if s[i] in count_s:
                count_s[s[i]] += 1
            if s[i] not in count_s:
                count_s[s[i]] = 1
            if t[i] in count_t:
                count_t[t[i]] += 1
            if t[i] not in count_t:
                count_t[t[i]] = 1
        

        return count_s == count_t

sol = Solution()

print(sol.isAnagram(s = "anagram", t = "nagaram"))

print(sol.isAnagram(s = "rat", t = "car"))