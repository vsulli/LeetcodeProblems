# leetcode #242

class Solution:
    def isAnagram(self, s: str, t: str)->bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        for n in count:
            if n != 0:
                return False
        return True


sol = Solution()
print(sol.isAnagram(s = "anagram", t = "nagaram"))
