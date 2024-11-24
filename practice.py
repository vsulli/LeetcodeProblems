# 242 Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str)->bool:
        # check if same length]
        if len(s) != len(t):
            return False
        # create an array for each letter
        count = [0] * 26
        for i in range(len(s)):
            # increase and decrease that letter index for s and t
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        for i in range(len(count)):
            if count[i] != 0:
                return False
        return True
    


        

sol = Solution()
print(sol.isAnagram(s = "anagram", t = "nagaram"))
print(sol.isAnagram("rat", t = "car"))